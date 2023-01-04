import re

import requests
#
#
# st = '''
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9
# Cache-Control: max-age=0
# Connection: keep-alive
# Cookie: JSESSIONID=73EAEE420FDCF6B7734721E10E85C4BF; _gscu_15322769=92202765o1rtxy20; _gscbrs_15322769=1; _gscs_15322769=922027658m3asu20|pv:1; Hm_lvt_d59e2ad63d3a37c53453b996cb7f8d4e=1592202768; Hm_lpvt_d59e2ad63d3a37c53453b996cb7f8d4e=1592202768
# Host: zxgk.court.gov.cn
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
'Cookie': 'JSESSIONID=73EAEE420FDCF6B7734721E10E85C4BF; _gscu_15322769=92202765o1rtxy20; _gscbrs_15322769=1; _gscs_15322769=922027658m3asu20|pv:1; Hm_lvt_d59e2ad63d3a37c53453b996cb7f8d4e=1592202768; Hm_lpvt_d59e2ad63d3a37c53453b996cb7f8d4e=1592202768',
'Host': 'zxgk.court.gov.cn',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'

}
response = requests.get('http://zxgk.court.gov.cn/xgl/',headers=headers)

print(response.text)