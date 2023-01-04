import requests
import re
from urllib import parse

from fontTools.ttLib import TTFont
from parsel import Selector
from lxml import etree

def dict_my(filename):
    font = TTFont(filename)
    cmap = font['cmap'].getBestCmap()
    newmap = {}
    ocr = '''
    1234567890店中美家馆小车大市公酒行国品发电金心业商司
    超生装园场食有新限天面工服海华水房饰城乐汽香部利子老艺花专东肉菜学
    福饭人百餐柔务通味所山区门药银农龙停尚安广鑫一容动南具源兴鲜记时机
    烤文康信果阳理锅宝达地儿衣特产西批坊州牛佳化五米修爱北养卖建材三会
    鸡室红站德王光名丽油院堂烧江社合星货型村自科快便日民营和活童明器烟
    育宾精屋经居庄石顺林尔县手厅销用好客火雅盛体旅之鞋辣作粉包楼校鱼平
    彩上吧保永万物教吃设医正造丰健点汤网庆技斯洗料配汇木缘加麻联卫川泰
    色世方寓风幼羊烫来高厂兰阿贝皮全女拉成云维贸道术运都口博河瑞宏京际
    路祥青镇厨培力惠连马鸿钢训影印助窗布富牌头四多妆吉苑沙恒降春干饼氏
    里二管诚制售嘉长轩杂副清计黄讯太鸭号街交与叉附近层旁对巷栋环省桥湖
    段乡厦府铺内侧元购前幢滨处向座下県凤港开关景泉塘放昌线湾政步宁解白
    田町溪十八古双胜本单同九迎第台玉锦底后七斜期武岭松角纪朝峰六振珠局
    岗洲横边济井办汉代临弄团外塔杨铁浦字年岛陵原梅进荣友虹央桂沿事津凯
    莲丁秀柳集紫旗张谷的是不了很还个也这我就在以可到错没去过感次要比觉
    看得说常真们但最喜哈么别位能较境非为欢然他挺着价那意种想出员两推做
    排实分间甜度起满给热完格荐喝等其再几只现朋候样直而买于般豆量选奶打
    每评少算又因情找些份置适什蛋师气你姐棒试总定啊足级整带虾如态且尝主
    话强当更板知己无酸让入啦式笑赞片酱差像提队走嫩才刚午接重串回晚微周
    值费性桌拍跟块调糕
    '''.replace('\n', '').replace(' ','')
    content = font['glyf'].glyphs
    keys = list(content.keys())[2:]
    real_dict = {key: value for key, value in zip(keys, ocr)}
    new_dict = {}
    for key, value in real_dict.items():
        key_ = key.replace('uni', '&#x')
        new_dict[key_] = value
    return new_dict

# st='''
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9
# Cache-Control: max-age=0
# Connection: keep-alive
# Cookie: navCtgScroll=0; t_lxid=171ecf1b328c8-0c7f43d2186c4f-87f133f-100200-171ecf1b328c8-tid; _lxsdk=171ecf1b328c8-0c7f43d2186c4f-87f133f-100200-171ecf1b328c8; _hc.v=c0f8882c-9fa8-2f3b-3645-359f37234fac.1588818197; fspop=test; cy=2; cye=beijing; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=172b57636e3c8-027300d742dd43-87f133f-100200-172b57636e3c8; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1592182325; s_ViewType=10; _lxsdk_s=172b57636e4-b66-7dd-a61%7C%7C74; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1592182464
# Host: www.dianping.com
# Referer: http://www.dianping.com/beijing/ch10
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36
# '''
# pattern = '^(.*?):[\s]*(.*?)$'
# headers = ""
# for line in st.splitlines():
#     headers += (re.sub(pattern,'\'\\1\': \'\\2\',',line)) + '\n'
# print(headers[:-2])

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'navCtgScroll=0; t_lxid=171ecf1b328c8-0c7f43d2186c4f-87f133f-100200-171ecf1b328c8-tid; _lxsdk=171ecf1b328c8-0c7f43d2186c4f-87f133f-100200-171ecf1b328c8; _hc.v=c0f8882c-9fa8-2f3b-3645-359f37234fac.1588818197; fspop=test; cy=2; cye=beijing; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=172b57636e3c8-027300d742dd43-87f133f-100200-172b57636e3c8; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1592182325; s_ViewType=10; _lxsdk_s=172b57636e4-b66-7dd-a61%7C%7C74; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1592182464',
'Host': 'www.dianping.com',
'Referer': 'http://www.dianping.com/beijing/ch10',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
}
url='http://www.dianping.com/shop/G7Uv5jp1mP1C6SlN'
resp = requests.get(url,headers=headers)
sel = Selector(resp.text)
# 提取页面加载的所有css文件路径
css_path = sel.css('link[rel=stylesheet]::attr(href)').extract()
woffs = []
html = resp.text
for c in css_path:
    # 拼接正确的css文件路径
    css_url = parse.urljoin(url, c)
    # 向css文件发起请求
    css_resp = requests.get(css_url)
    # 匹配css文件中的woff文件路径
    woff_path = re.findall("src:url(\(.*?\));", css_resp.text)
    if woff_path:
        # 如故路径存在则添加到woffs列表中
        woffs += woff_path
print(woffs[::2][:-1])
# new_woffs = []
count = 0
dict_ = {}
for i in woffs[::2][:-1]:
# woff_url = 'http://www.dianping.com/shop/G7Uv5jp1mP1C6SlN' + woffs.pop()
    ls = i[2:-2].split('.eot')
    woff_url = "https:"+ls[0]+'.woff'
    woff = requests.get(woff_url)
    filename = woff_url.split('/')[-1]
    with open(filename, 'wb') as f:
        # 将文件保存到本地
        f.write(woff.content)

    dict_['dict_'+str(count)] = dict_my(filename)
    count+=1
    for key ,value in dict_.items():
        for key,value in dict_[key].items():
            if key in html:
                html = html.replace(key,value)
            else:
                pass


html2 = etree.HTML(html)
comment = re.findall('reviewCount" class="item"> <d class="num">(.*?)条评论',html,re.S)#评论
num = re.sub('\D','',comment[0])
address = re.findall('id="address">(.*?)\)',html,re.S)
word = re.sub('[a-z]|\<|\=|\"|\>|\;|\/|\'','',address[0])# 使用TTFont库打开刚才下载的woff文件
word = word.replace(' ','')+str(')')
