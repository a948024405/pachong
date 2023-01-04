import time
import requests
import json
# e[$_CJEl(1)] = 160,
# e[$_CJEl(64)] = 260;
# for (var a = r / 2, _ = 0; _ < 52; _ += 1) {
#     var c = Ut[_] % 26 * 12 + 1
# , u = 25 < Ut[_] ? a: 0
# , l = o[$_CJFA(27)](c, u, 10, a);
# s[$_CJFA(81)](l, _ % 26 * 10, 25 < _ ? a: 0);
# }
import execjs

js = execjs.compile(open('w参数.js','r',encoding="utf-8").read())
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

    headers = {
     "Accept": "*/*",
     "Accept-Encoding": "gzip, deflate",
     "Accept-Language": "zh-CN,zh;q=0.9",
     "Connection": "keep-alive",
     "Host": "api.geetest.com",
     "Referer": "https://www.geetest.com/",
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
     "sec-ch-ua-mobile": "?0",
     "Sec-Fetch-Dest": "script",
     "Sec-Fetch-Mode": "no-cors",
     "Sec-Fetch-Site": "same-site",
    'Cookie': 'GeeTestAjaxUser=551e265a092119a6f39cc7656a5c1c16; GeeTestUser=8598c749beb765027ca92c535b3d01fd; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218561d7bea3633-0e2e24a96708378-c3f3568-2073600-18561d7bea4b05%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.geetest.com%2Fpictures%2Fgt%2F09b7341fb%2F09b7341fb.jpg%22%7D%2C%22%24device_id%22%3A%2218561d7bea3633-0e2e24a96708378-c3f3568-2073600-18561d7bea4b05%22%7D; Hm_lvt_25b04a5e7a64668b9b88e2711fb5f0c4=1672383808; Hm_lpvt_25b04a5e7a64668b9b88e2711fb5f0c4=1672383808',

     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
}
    gt, challenge = get_ge_chalg()
    print(
        gt,challenge
    )
    w = js.call('getW',gt,challenge)
    print(w)
    data = {
        'gt': '019924a82c70bb123aae90d483087f94',
        'challenge': 'd87a62f3e897917e3df0ef7b77584416',
        'lang': 'zh-cn',
        'pt': '0',
        'client_type': 'web',
        'w':w

    }
    print(data)
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
    }
    # url0 = "https://apiv6.geetest.com/gettype.php"
    # res0 = requests.get(url0,data={
    #     'gt':gt
    # },headers=headers)
    # print(res0.text) #ok
    #
    # url1 = 'https://apiv6.geetest.com/get.php'
    # response1 = requests.get(url1, data=data, headers=headers)
    # print(response1.text)
    #
    # url = 'https://api.geetest.com/ajax.php'
    # response = requests.get(url, data=data, headers=headers)
    # print(response.text)
    # #
    # # time.sleep(1)
    # url1 = 'https://api.geetest.com/get.php'
    # response1 = requests.get(url1, data=data1, headers=headers)
    # print(response1.text)

    # fullbg = json.loads(response.text[1:-1])['fullbg']


get_img_url_download()

