

def fuckEncode(str1):
    res = ''
    for i in str1:

        res1 = hex(ord(i))
        if len(res1) > 4:
            res += '\\u' + res1[2:]
        else:
            res += '\\u00' + res1[2:]
    return res

print(fuckEncode("userresponse"))