

a='''
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Host: api.geetest.com
Referer: https://www.geetest.com/
sec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"
sec-ch-ua-mobile: ?0
Sec-Fetch-Dest: script
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-site
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
'''


c = []
results = a.split("\n")[1:-1]
for result in results:
    b = result.split(": ")
    c.append("\""+b[0]+"\""+": \""+b[1]+"\",")
print("复制以下内容：")
print("headers = {")
for cc in c:
    print("     "+cc)
print("}")
