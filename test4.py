#encoding:utf8
__author__ = 'gold'

import re
text = "JGood is a handsome boy, he is cool, clever, and so on..."
print(re.sub(r'\s+', lambda m:'['+m.group(0)+']', text,0))
# JGood[ ]is[ ]a[ ]handsome[ ]boy,[ ]he[ ]is[ ]cool,[ ]clever,[ ]and[ ]so[ ]on...
print(re.search(r"(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5]\.)","192.168.1.1").group())
print(re.search(r"^(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])$","1.2.3.100").group(3))