

from fontTools.ttLib import TTFont
font = TTFont('rrcttf9b8db3122f64b3d19d04d7fcab2dc4c4.woff')




"""
0 --> 正常的数字
编码   正常
1 -- >  2

"""

relation_table = {"zero": "0", "one": "2", "two": "1", "three": "4", "four": "3", "five": "8", "seven": "7","eight": "5", "six": "6", "nine": "9"}
print(font.getBestCmap())
_code = font.getBestCmap()
new_code = {}
for code,name in _code.items():
    code_str = str(code-48)
    # new_code[name] = code_str
    # zx = dict(zip(relation_table.values(), relation_table.keys()))
    get_real_data = relation_table[name]
    print(get_real_data)
    new_code[code_str] =get_real_data
print(new_code)


# maps = [new_code[i] for i in uni_list[1:]]
# print(maps)
# font_dict = dict(zip(new_code.values(),maps))
# print(font_dict)





