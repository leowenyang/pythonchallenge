# coding=UTF-8

secretChar="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def CharPlus2(char):
    if (ord('a') <= ord(char)) and (ord(char) <= ord('x')):
        char = chr(ord(char)+2)
        return char
    if (char == 'y'):
        return 'a'
    if (char == 'z'):
        return 'b'
    else:
        return char

clearChar=""
for char in secretChar:
    clearChar += CharPlus2(char)
print clearChar

import string
websit="http://www.pythonchallenge.com/pc/def/"
print "next websit adress is:"
pagesit="map"
table=string.maketrans("abcdefghigklmnopqrstuvwxyz","cdefghigklmnopqrstuvwxyzab")
print websit+pagesit.translate(table)+".html"
