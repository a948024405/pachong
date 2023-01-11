import io
import time
from pathlib import Path

import requests
import json
from pathlib import Path

from PIL import Image
import execjs

js = execjs.compile(open('w参数2.js','r',encoding="utf-8").read())
ts = int(time.time())
headers = {
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
def get_ge_chalg():

    url = f'https://www.geetest.com/demo/gt/register-slide?t={ts}'
    response = requests.get(url,headers = headers)
    gt, challenge = response.json()['gt'],response.json()['challenge']
    return gt, challenge

def get_img_url_download():

    headers =  {
     "Accept": "*/*",
     "Accept-Language": "zh-CN,zh;q=0.9",
     "Connection": "keep-alive",
     "Host": "api.geetest.com",
     # 'Cookie': 'GeeTestAjaxUser=c546f6b92b0f67921d260eaa188dc9ed;GeeTestUser=b550a4d54c18a2db2944771585949069',
     "Referer": "https://www.geetest.com/",
     "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
     "sec-ch-ua-mobile": "?0",
     "Sec-Fetch-Dest": "script",
     "Sec-Fetch-Mode": "no-cors",
     "Sec-Fetch-Site": "same-site",
     "Content-Type": "application/x-www-form-urlencoded",
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
}


    gt, challenge = get_ge_chalg()

    data = {
        'gt': gt,
        'challenge': challenge,
        'lang': 'zh-cn',
        'pt': '0',
        'client_type': 'web',
        # 'w':w,

    }
    data1 = {
        's_next': 'true',
        'type': 'slide3',
        'gt': gt,
        'challenge': challenge,
        'lang': 'zh-cn',
        'https': 'true',
        'protocol': 'https://',
        'offline': 'false',
        'product': 'custom',
        'api_server': 'api.geetest.com',
        'isPC': 'true',
        'autoReset': 'true',
        'area': '#area',
        'bg_color': 'gray',
        'width': '278px',
        'callback': 'geetest_1'

    }

    #过点击验证
    url = 'https://api.geetest.com/ajax.php'
    requests.get(url, params=data, headers=headers)

    url1 = 'https://api.geetest.com/get.php'
    response1 = requests.get(url1, params=data1, headers=headers)

    backJson = json.loads(response1.text[len('geetest_1') + 1:-1])
    fullbg ="https://static.geetest.com/" + backJson['fullbg']

    pic = requests.get(fullbg)
    content = pic.content
    #还原背景图片
    parse_bg_captcha(content,False,'fullbg.png')

    #下载滑块小图
    slicePg =   "https://static.geetest.com/" + backJson['slice']

    #背景图 缺口图

    sliceContent = requests.get(slicePg).content
    with open('slice.png','wb') as f:
        f.write(sliceContent)

    bgBg =   "https://static.geetest.com/" + backJson['bg']
    bgContent = requests.get(bgBg).content

    parse_bg_captcha(bgContent, False, 'bg.png')

    return json.loads(response1.text[len('geetest_1') + 1:-1]),gt, challenge + '1b'

def parse_bg_captcha(img, im_show=False, save_path=None):
    """
    滑块乱序背景图还原
    :param img: 图片路径str/图片路径Path对象/图片二进制
        eg: 'assets/bg.webp'
            Path('assets/bg.webp')
    :param im_show: 是否显示还原结果, <type 'bool'>; default: False
    :param save_path: 保存路径, <type 'str'>/<type 'Path'>; default: None
    :return: 还原后背景图 RGB图片格式
    """
    if isinstance(img, (str, Path)):
        _img = Image.open(img)
    elif isinstance(img, bytes):
        _img = Image.open(io.BytesIO(img))
    else:
        raise ValueError(f'输入图片类型错误, 必须是<type str>/<type Path>/<type bytes>: {type(img)}')
    # 图片还原顺序, 定值
    _Ge = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43,
           42, 12, 13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]
    w_sep, h_sep = 10, 80

    # 还原后的背景图
    new_img = Image.new('RGB', (260, 160))

    for idx in range(len(_Ge)):
        x = _Ge[idx] % 26 * 12 + 1
        y = h_sep if _Ge[idx] > 25 else 0
        # 从背景图中裁剪出对应位置的小块
        img_cut = _img.crop((x, y, x + w_sep, y + h_sep))
        # 将小块拼接到新图中
        new_x = idx % 26 * 10
        new_y = h_sep if idx > 25 else 0
        new_img.paste(img_cut, (new_x, new_y))

    if im_show:
        new_img.show()
    if save_path is not None:
        save_path = Path(save_path).resolve().__str__()
        new_img.save(save_path)
    return new_img





test,gt,challenge = get_img_url_download()
c = test['c']
s = test['s']
challenge = test['challenge']

import ddddocr
import random
slide = ddddocr.DdddOcr(det=False, ocr=False)

with open('fullbg.png', 'rb') as f:
    target_bytes = f.read()

with open('bg.png', 'rb') as f:
    background_bytes = f.read()

#
res = slide.slide_comparison(target_bytes, background_bytes)
target_X = res['target'][0]
print(target_X)



arr = [[-40, -23, 0], [0, 0, 0]]
x = 0
t = 0
for i in range(target_X):
    randomY = t % 100 * -1
    if x>= target_X -10:
        arr.append([ target_X -10 , randomY, t])
        break

    randomX = random.randint(2,4)
    x += randomX
    t +=  random.randint(0, 70)
    if (i % 10 == 0 and i != 0):
        x -= 6
        arr.append([x, randomY, t])
    if x >= target_X - 10:
        arr.append([x, randomY, t])
        t +=  random.randint(0, 50)
        continue
    arr.append([x , randomY , t])

print(gt, challenge,arr,c,s)
w = js.call('getW', gt, challenge, arr, c, s)
print(w)

data = {
    'gt': gt,
    'challenge':challenge,
    'lang': 'zh-cn',
    '$_BCw': '0',
    'client_type': 'web',
    'w': w
}
print(data)
response = requests.get("https://api.geetest.com/ajax.php",params=data,headers =  {
     "Accept": "*/*",
     "Accept-Language": "zh-CN,zh;q=0.9",
     "Connection": "keep-alive",
     "Host": "api.geetest.com",
     # 'Cookie': 'GeeTestAjaxUser=c546f6b92b0f67921d260eaa188dc9ed;GeeTestUser=b550a4d54c18a2db2944771585949069',
     "Referer": "https://www.geetest.com/",
     "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
     "sec-ch-ua-mobile": "?0",
     "Sec-Fetch-Dest": "script",
     "Sec-Fetch-Mode": "no-cors",
     "Sec-Fetch-Site": "same-site",
     "Content-Type": "application/x-www-form-urlencoded",
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
})

print(response.text)



