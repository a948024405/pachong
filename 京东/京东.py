import re
import requests

import json

headers_str={
"Accept": "*/*",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9",
"Connection": "keep-alive",
"Cookie": "__jdu=1563183769347597531227; shshshfpb=0d8969df62d26a27f1835053dd0424eee8443b20128e451985bb57de89; shshshfpa=e2c255df-bdb8-bc32-6282-f4c16f3d8db2-1563183771; pinId=jIEXxkISPx-yJYdVymeBZrV9-x-f3wj7; TrackID=1rcLCx-B94LrkrfBlYgdnJSCqR4CZOILM-aFlG945lsTVbSbZlvkbzMs4g9Eq_W0Kr0csefUQyjeYf9eP0pJtqnA9EucXpljFPn5DGf3bPTs; user-key=18c4357a-7741-4459-a184-59c071c01400; cn=1; unpl=V2_ZzNtbRZWERF0X0VRKBwJDWIEEg8SAkYTdQxFUHMRVANuUUIIclRCFnQUR1NnGFwUZwMZXEFcQRdFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsdWwdnChBbRV9BEHMMTlJ%2fG1wGZAUibUVncyVwAENSeyldNWYzUAkeUkITcg1CGXsdWwdnChBbRV9BEHMMTlJ%2fG1wGZAUiXHJU; areaId=4; ipLoc-djd=4-113-9786-0; jwotest_product=99; __jdv=76161171|direct|-|none|-|1592294972608; __jda=122270672.1563183769347597531227.1563183769.1591756267.1592294973.23; __jdc=122270672; shshshfp=17478619b4a9b094f57d4dda34a19ed7; 3AB9D23F7A4B3C9B=LFXZ53OQIMUKAWH5R23XQAZ7IYLLV3PAWMSLM3ZD2THYKKBGSCS2YMHFRVCXB2DP2MCSQLRODRNETMIS3ZUJNWDXAQ; JSESSIONID=DECF6BBA68B05E1997D7B92699CB3B9D.s1; shshshsID=c6a9f7c2e5de04a4b32445e15088b721_6_1592295467564; __jdb=122270672.6.1563183769347597531227|23.1592294973",
"Host": "club.jd.com",
"Referer": "https://item.jd.com/1833238.html",
"Sec-Fetch-Dest": "script",
"Sec-Fetch-Mode": "no-cors",
"Sec-Fetch-Site": "same-site",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
}

url = 'https://club.jd.com/comment/productPageComments.action'
param = {
"productId": "1833238",
"score": "0",
"sortType": "5",
"page": "0",
"pageSize": "10",
"isShadowSku": "0",
"fold": "1",

}
# js = '{"conditions":[{"type":1,"value":"xian"},{"label":"入住日期","type":2,"value":"2020-06-16"},{"label":"离店日期","type":3,"value":"2020-06-17"}],"defaultKeyword":"","onlyReturnTotalCount":false,"pageIndex":0,"pageSize":12,"returnFilterConditions":true,"returnGeoConditions":true,"url":""}'
# js = json.dumps(js)
# print(type(js))
response = requests.get(url,headers=headers_str,params = param)
print(response.text)