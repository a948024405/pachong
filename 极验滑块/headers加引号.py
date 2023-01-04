

a='''
api_server: "apiv6.geetest.com"
area: "#area"
aspect_radio: {slide: 103, click: 128, voice: 128, beeline: 50}
beeline: "/static/js/beeline.1.0.1.js"
bg_color: "gray"
cc: 6
challenge: "3f060042e405401f6ee334091478762a"
click: "/static/js/click.3.0.7.js"
fullpage: "/static/js/fullpage.9.1.1.js"
geetest: "/static/js/geetest.6.0.9.js"
gt: "019924a82c70bb123aae90d483087f94"
https: true
i: "6371!!7659!!CSS1Compat!!1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!2!!3!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!1!!-1!!-1!!-1!!1!!1!!0!!0!!1920!!344!!1918!!1078!!zh-CN!!zh-CN,zh!!-1!!1!!24!!Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36!!1!!1!!1920!!1080!!1920!!1080!!1!!1!!1!!-1!!Win32!!0!!-8!!e259b31c460afab4e3d3aa7b2768d71e!!0!!internal-pdf-viewer,mhjfbmdgcfjbbpaeojofohoefgiehjai,internal-nacl-plugin!!0!!-1!!0!!6!!Arial,ArialBlack,ArialNarrow,BookAntiqua,BookmanOldStyle,Calibri,Cambria,CambriaMath,Century,CenturyGothic,ComicSansMS,Consolas,Courier,CourierNew,Garamond,Georgia,Helvetica,Impact,LucidaConsole,LucidaSansUnicode,MicrosoftSansSerif,MonotypeCorsiva,MSGothic,MSPGothic,MSReferenceSansSerif,MSSansSerif,MSSerif,PalatinoLinotype,SegoePrint,SegoeScript,SegoeUI,SegoeUILight,SegoeUISemibold,SegoeUISymbol,Tahoma,Times,TimesNewRoman,TrebuchetMS,Verdana,Wingdings,Wingdings2,Wingdings3!!1672391196653!!-1!!-1!!-1!!12!!-1!!-1!!-1!!5!!-1!!-1"
new_captcha: true
next_width: "278px"
offline: false
product: "custom"
protocol: "https://"
slide: "/static/js/slide.7.8.9.js"
static_servers: (2) ["static.geetest.com/", "dn-staticdown.qbox.me/"]
type: "fullpage"
voice: "/static/js/voice.1.2.2.js"
width: "300px"
ww: true
__proto__: Object
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
