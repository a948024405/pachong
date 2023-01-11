
from fontTools.ttLib import TTFont

font = TTFont('file (3).woff')

# print(font.keys())

# font.saveXML('file.xml')

code_name_map = font.getBestCmap()  #  key  10进制
# print(code_name_map)

# print(font.getGlyphOrder())
# print(font.getGlyphID('uni32'))
# print(font['glyf']['uni32'])
# 动态字体的处理方式  就是对比字形  坐标万变不离其中
# print(font['glyf']['uni32'].coordinates)

# 使用字形坐标  描绘文字

import matplotlib.pyplot as plt

# pip install matplotlib

coordinate = list(font['glyf']['uni56DB'].coordinates)
fig, ax = plt.subplots() # 返回的是子画布的对象
x = [i[0] for i in coordinate]
y = [i[1] for i in coordinate]
plt.fill(x, y, color="red", alpha=1)
# 取消边框
for key, spine in ax.spines.items():
     if key == 'right' or key == 'top' or key == 'bottom' or key == 'left':
         spine.set_visible(False)
plt.plot(x, y)
# 取消坐标：
plt.axis('off')
# plt.savefig('uniF0D5.png')
plt.show()






