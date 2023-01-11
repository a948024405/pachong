import re
from io import BytesIO
import execjs
from fontTools.ttLib import TTFont
import requests
from lxml import etree


class Xl():
    def __init__(self):
        self.headers = {
                "Host": "www.renrenche.com",
                "Pragma": "no-cache",
                "Referer": "https://www.renrenche.com/bj/ershouche/p2/?&plog_id=838083390d4b077a45852d11065f60ad",
                "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
        self.maps = lambda x: x[0] if x else x

    def get_index(self):
        com_cookie = {}
        url = 'https://www.renrenche.com/bj/ershouche/p2/?&plog_id=838083390d4b077a45852d11065f60ad'
        res = requests.get(url,headers=self.headers)
        com_cookie.update(res.cookies.get_dict())
        arg1 = re.findall("arg1='(.*)'",res.text)
        arg1 =arg1[0] if arg1 else arg1
        with open('acw_tc.js',encoding='utf-8') as f:
            acw_tc = f.read()
        acw_tc_v2 = execjs.compile(acw_tc).call('ps',arg1)
        com_cookie.update({
            'acw_sc__v2':acw_tc_v2
        })
        # 第二次访问 携带cookie
        res2 = requests.get(url,headers=self.headers,cookies=com_cookie).text
        # 提取字体文件
        with open('index.html','w' ,encoding='utf-8') as f:
            f.write(res2)
        return res2

    def get_font(self,text):
        font_url = re.search("url\('(.*\.woff)'\)",text).group(1)
        return font_url

    def woff_font(self,font_url):
        # 获取真实字体对应关系
        resp = requests.get(font_url)
        open('xxx.woff', 'wb').write(resp.content)
        wff_data = BytesIO(resp.content)
        font = TTFont(wff_data)
        uni_list = font.getGlyphOrder()
        code_ = font.getBestCmap()
        new_code = {}
        for code, name in code_.items():
            code_str = str(code - 48)
            new_code[name] = code_str
        mapping_list = [new_code[_] for _ in uni_list[1:]]
        font_dict = dict(zip(new_code.values(), mapping_list))
        return font_dict

    def parse_data(self,font_dict,text):
        html = etree.HTML(text)
        items = html.xpath('//ul[@class="row-fluid list-row js-car-list"]/li')
        for i in items:
            tilte = self.maps(i.xpath('.//h3/text()'))
            trans_title = ''.join([i if not i.isdigit() else font_dict[i] for i in tilte])
            print(trans_title)

    def run(self):
        text = self.get_index()
        # 使用测试接口
        # with open('index.html', encoding='utf-8') as f:
        #     text = f.read()
        font_url = self.get_font(text)
        font_dict = self.woff_font(font_url)
        self.parse_data(font_dict,text)

if __name__ == '__main__':
    Xl().run()

