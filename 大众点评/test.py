import requests
import re
from urllib import parse

from fontTools.ttLib import TTFont
from parsel import Selector

base_font=['1','2','3','4','5','6','7','8']

font = TTFont('64c220e4.woff')
cmap = font['cmap'].getBestCmap()
newmap = {}
ocr='''
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
'''.replace('\n','')
# #转16进制
# for key,value in cmap.items():
#     key = hex(key)
#     value = value.replace('uni','')
#     a = 'u'+'0'*(4-len(value))+value
#     newmap[key]  = a
# #删除第一个没用的
# newmap.pop('0x78')
# #加上前缀u变成unicode
# for i ,j in newmap.items():
#     newmap[i] = eval("u"+"\'\\"+j+"\'")
content = font['glyf'].glyphs
keys = list(content.keys())[2:]
real_dict={key:value for key,value in zip(keys,ocr)}
new_dict={}
for key,value in real_dict.items():
    key_ = key.replace('uni','&#x')
    new_dict[key_] = value
    # for key,value in new_dict.items():
    #     if key in st:
    #         st = st.replace(key,value)
    #     else:
    #         pass
