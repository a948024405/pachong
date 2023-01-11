## 文本混淆章节

### 1.  文本混淆简介

简单而言就是利用前端技术干扰，页面可以正常展示，而使用爬虫下载后无法提取正常的数据。

#### 1.1 常见的干扰方式

+ 字体反爬

### 2. 字体反爬

#### 2.1 字体反爬简介

​		在 `CSS3 `之前，`Web` 开发者必须使用用户计算机上已有的字体。目前的技术开发者可以使用`@font-face`为网页指定字体，开发者可将心仪的字体文件放在 Web 服务器上，并在` CSS` 样式中使用它。用户使用浏览器访问 `Web应用`时，对应的字体会被浏览器下载到用户的计算机上。

**注：**使用自动化`selenium`也无法获取正常的数据

### 3.  某习字体反爬实践

#### 3.1 逆向目标

+ 首页：https://www.shixiseng.com/
+ 目标：https://www.shixiseng.com/interns?keyword=产品&city=全国&type=intern&from=menu
+ 逆向：薪酬字体

#### 3.2 逆向分析

##### 3.2.1 网页分析

+ 打开网站可以发现，价格的字体是乱码

![image-20220830135453763](images\image-20220830135453763.png)

##### 3.2.2 页面处理

+ 在页面源代码中搜索`font-face`关键字，可以发现字体文件在网页源代码中

![image-20220830140449959](images\image-20220830140449959.png)

+ 可以在网络抓包里面进行筛选，可以发现这里面有对应的字体文件加载地址，由后端返回

  ![image-20220830140631194](images\image-20220830140631194.png)

+ 对于字体文件，可以直接使用工具解析
  + 在线地址：http://font.qqe2.com/
    + 使用方式:
      + 下载字体文件到本地目录
      + 访问在线工具网站，点击左上角打开，找到本地目录字体文件即可

![image-20220830141035825](images\image-20220830141035825.png)

##### 3.3.3 字体分析

正常在网页里面展示的薪酬是：![image-20220830141940433](images\image-20220830142004643.png)

+ 下载后的页面元素

![image-20220830141754024](images\image-20220830141754024.png)

+ 解析的字体文件

  ![image-20220830141835755](images\image-20220830141835755.png)

+ `woff`文件转化成`xml`文件进行分析 `cmap`是关键 原来是`unicode`码

  ![image-20220830153625467](images\image-20220830153625467.png)



#### 3.3 逆向结果

![image-20220830153726609](images\image-20220830153726609.png)

##### 3.3.1 完整code

```python
class Sxs():
    def __init__(self):
        self.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
    }

    def get_html(self):
        # 第1步：获取html，且存为html文件以便后面研究使用
        url = 'https://www.shixiseng.com/interns?keyword=%E4%BA%A7%E5%93%81&city=%E5%85%A8%E5%9B%BD&type=intern&from=menu'
        ret = requests.get(url=url, headers=self.headers).text
        with open('index.html', 'w', encoding='utf8') as f:
            f.write(ret)
        return ret

    def get_font(self,ret):
        # 第2步：下载html配套的ttf文件
        font_url = re.findall('src: url\((.*?)\);', ret)
        f_url = 'https://www.shixiseng.com' + font_url[0] if font_url else font_url
        font_data = requests.get(f_url)
        with open('file.woff', 'wb') as f:
            f.write(font_data.content)

    def get_font_data(self,ttf):
        font_dict = {}
        # font = TTFont("file.woff")
        font = TTFont(ttf)
        cmap = font.get("cmap").getBestCmap()
        for k, v in cmap.items():
            if v[3:]:
                content = "\\u00" + v[3:] if len(v[3:]) == 2 else "\\u" + v[3:]
                real_content = content.encode('utf-8').decode('unicode_escape')
                k_hex = hex(k)
                # 网页返回的字体是以&#x开头  ，换成以这个开头，下面代码就是直接替换
                real_k = k_hex.replace("0x", "&#x")
                font_dict[real_k] = real_content
        return font_dict

    def put_html(self,ttf_dict):
        with open("index.html", "r", encoding="utf-8") as f:
            html = f.read()
            for k, v in ttf_dict.items():
                html = html.replace(k, v)
            return html

    def get_data(self,html):
        html = etree.HTML(html)
        li_list = html.xpath("//div[@class='intern-wrap intern-item']")
        for li in li_list:
            title = "".join(li.xpath(".//div[@class='f-l intern-detail__job']//a/text()")[0].split())
            price = "".join( li.xpath(".//div[@class='f-l intern-detail__job']//span[@class='day font']/text()")[0].split())
            name = li.xpath('.//a[@class="title ellipsis"]/text()')[0]
            print(title, price,name)

    def main(self):
        # 第1步：获取html，且存为html文件以便后面研究使用
        ret = self.get_html()
        # 第2步：下载html配套的ttf文件
        self.get_font(ret)
        # 第3步：提取ttf中摄影的数据
        font_dict = self.get_font_data('file.woff')
        # 第4步：对下载（HTML内容）进行替换
        html = self.put_html(font_dict)
        # 第5步：使用xpath提取想要的数据
        data = self.get_data(html)
        print(data)

if __name__ == '__main__':
    Sxs().main()
```



### 4. 字体解析工具

**字体读取工具**

```
链接：https://pan.baidu.com/s/1c57IHzTN0aPVgIO5NMq3OA 
提取码：1234
```

**4.1 工具安装**

```
pip install fontTools  # 使用这个包处理字体文件
```

#### 4.2 字体读取

```python
from fontTools.ttLib import TTFont
# 加载字体文件：
font = TTFont('file.woff')
# 转为xml文件：
font.saveXML('file.xml')
```

#### 4.3 节点读取

```python
from fontTools.ttLib import TTFont
# 加载字体文件：
font = TTFont('file.woff')
kv = font.keys()
print(kv)
```

字体文件不仅包含字形数据和点信息，还包括字符到字形映射、字体标题、命名和水平指标等，这些信息存在对应的表中：

| 表   | 作用           |
| ---- | -------------- |
| cmap | 字符到字形映射 |
| glyf | 字形数据       |
| head | 字体标题       |
| hhea | 水平标题       |
| hmtx | 水平指标       |
| loca | 索引到位置     |
| maxp | 最大限度的     |
| name | 命名           |
| post | 后记           |

#### 4.4 获取请求到的字体code和name的对应关系

```
code_name_map = font_aa.getBestCmap()
```

#### 4.5 获取字体坐标信息

```python
font_aa = TTFont('file.woff')
# 获取请求到的字体形状
glyf = font_aa['glyf']
#font['glyf'][字体编码].coordinates
font_aa['glyf']['uni4E94'].coordinates
```



### 5. 某车字体反爬

#### 5.1 逆向目标

+ 首页：https://www.renrenche.com/
+ 目标：https://www.renrenche.com/bj/ershouche/p2/?&plog_id=838083390d4b077a45852d11065f60ad
+ 逆向：标题字体

#### 5.2 逆向分析

![image-20220830164839285](images\image-20220830164839285.png)

+ 打开网页源代码搜索`font-face`,查找字体文件

  ![image-20220830165032274](images\image-20220830165032274.png)

+ 分析字形关系

  ![image-20220830165555789](images\image-20220830165555789.png)



##### 5.2.1 原字形还原

请求字体链接，获取字体code和name的对应关系，然后遍历，获取网页中反爬文字的真实文字。

```python
relation_table = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "seven": "6","eight": "7", "six": "8", "nine": "9"}
def woff_font(font_url):
    '''获取字体真实对应关系'''
    newmap = {}
    resp = session.get(font_url)  # 请求字体链接
    woff_data = BytesIO(resp.content)
    font = TTFont(woff_data)  # 读取woff数据
    cmap = font.getBestCmap()  # 获取字体对应关系
    font.close()
    for k, v in cmap.items():
        value = v
        key = str(k - 48)  # 获取真实的key
        try:
            get_real_data = relation_table[value]
        except:
            get_real_data = ''
        if get_real_data != '':
            newmap[key] = get_real_data  # 将字体真实结果对应
    return newmap
```



#### 5.3 逆向代码

```
链接：https://pan.baidu.com/s/1uhqLb7pVkRjgHlwwMxEJVA 
提取码：1234
```







