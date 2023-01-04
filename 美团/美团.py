import base64
import datetime
import random
import re
import time
import zlib
from urllib.parse import urlparse

import requests
#
# st = '''
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.9
# Cache-Control: max-age=0
# Connection: keep-alive
# Cookie: uuid=fcdde24f08db40089d7a.1592203370.1.0.0; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=172b6b769c432-061f24806c5274-87f133f-100200-172b6b769c5c8; ci=1; rvct=1; __mta=88929700.1592203515425.1592203515425.1592203515425.1; client-id=a1af102a-52ee-497e-ae28-0be00f3df6aa; _lxsdk_s=172b6b769c8-00a-16b-eb4%7C%7C6
# Host: bj.meituan.com
# Referer: https://bj.meituan.com/
# Sec-Fetch-Dest: document
# Sec-Fetch-Mode: navigate
# Sec-Fetch-Site: same-origin
# Sec-Fetch-User: ?1
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36
# '''
# pattern = r"^(.*?):\s?(.*?$)"
#
# for line in st.splitlines():
#     print(re.sub(pattern, r'"\1": "\2",', line))
headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Cookie": "uuid=fcdde24f08db40089d7a.1592203370.1.0.0; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=172b6b769c432-061f24806c5274-87f133f-100200-172b6b769c5c8; ci=1; rvct=1; __mta=88929700.1592203515425.1592203515425.1592203515425.1; client-id=a1af102a-52ee-497e-ae28-0be00f3df6aa; _lxsdk_s=172b6b769c8-00a-16b-eb4%7C%7C6",
"Host": "bj.meituan.com",
"Referer": "https://bj.meituan.com/",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-User": "?1",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
}
def decode_token(token):
    # base64解码
    token_decode = base64.b64decode(token.encode())
    # 二进制解压
    token_string = zlib.decompress(token_decode)
    return token_string

# # 生成token
def encode_token():
    ts = round(time.time()*1000)
    # ts = int(datetime.now().timestamp() * 1000)
    print(ts,ts+100)
    token_dict ={
     "rId":100900,
     "ver":"1.0.6",
     "ts":ts,
     "cts":ts+100,
     "brVD":[1366,150],"brR":[[1366,768],[1366,768],24,24],
     "bI":["https://bj.meituan.com/meishi/","https://bj.meituan.com/"],
     "mT":[],
     "kT":[],
     "aT":[],
     "tT":[],
     "aM":"",
     "sign":"eJwljb1twzAQhXdxwZI6yfKPArAwVBkw3GUAWjzJZ4ukcDwa8A7ps0Qm8DzJHiGS6n14eD8ry2iPzoAarOA/kDzP1qP5+fj8fn0pRyEg9zEHOYhwyai4CPmc+ujQ1KAi00ThnWdzFVnSW1VdbtojSbZBD9FXhdOVKrXYqRSKsJRJUzdbtcxWxsi+2EzpfsIHzoVTZDEqJ/z7y5mcGQfnsGlH2LtLC7Dv3M7qetM1DazXO9C1Bg2rX6YVSB0="
     }
    print()
    encode = str(token_dict).encode()
    # 二进制压缩
    compress = zlib.compress(encode)
    # base64编码
    b_encode = base64.b64encode(compress)
    # 转为字符串
    token = str(b_encode, encoding='utf-8')
    return token
# for page in range(1000):

url = 'https://bj.meituan.com/meishi/api/poi/getPoiList'

for i in range(1,1000):
    abc = encode_token()
    data = {
        "cityName": "北京",
        "cateId": "0",
        "areaId": "0",
        "sort": "",
        "dinnerCountAttrId": "",
        "page": i,
        "userId": "",
        "uuid": "68b540db90a248d39cbd.1592269847.1.0.0",
        "platform": "1",
        "partner": "126",
        "originUrl": "https://bj.meituan.com/meishi/",
        "riskLevel": "1",
        "optimusCode": "10",
        "_token": abc
    }
    time.sleep(random.randint(3, 5))
    response = requests.get(url, headers=headers, params=data)
    print(response.text)
# _token = 'eJx1T12PmzAQ/C9+PRRjzGekPpCWEFKgCXcQjuoeAkmAAL7EdjCXqv+9PvUqtQ+VVjuzs6PR7g9AgwOYI1V1VFUB45GCOUAzdWYCBXAmN4ajacjAumOqWAHVv5qFdAWUNPsC5t8RNk0FGerLu5JI4bdimfaL8hfVdFnvnkBaQMP5hc0hLM+z4djy257MqtcBSs6aFsob/mMAMmF4kgkSuw/cfyD/M0fyFxnB2ppIdlyL/lwiLu7utskPkyiCdpkOwqVukLtpgP2dG+FhCqdiree12i3wYyH6jb4ibJMGHTqNwl7pmnDbUSSk357c02NoaV7sOSOBN26yr/0ifAt51cleRe113FJ/l2+tV7r0CzM9X0hywF5PwsqpDhuSeV19WT9Mb9Z0yzyS0UZzL/EuvnYMah2q8y7AMYv7yBgfvGVvP/fs3mSfoeWglC5EEkW26WHPf4bNarW/c4N+sw2n1E889q/0/LQvc+NeJLD+BH7+AoyflOs='
# print(decode_token(abc))
