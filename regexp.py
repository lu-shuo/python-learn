#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'正则表达式'

__author__ = 'Darren Lu'

import re
# 匹配返回match对象，不匹配返回None

# t = input('请输入：')

# # print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
# if re.match(r'^\d{3}-\d{3,8}$', t):
#     print('OK')
# else:
#     print('Failed')

# print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))
re_tel = re.compile(r'^(\d{3})-(\d{3,8})$')
re_mail = re.compile(r'^[\da-zA-Z\.]+\@[a-z]+\.com$')
print(re_mail.match('Hellolus@hotmail.com'))
# m = re_tel.match('181-68698679')
# print(m)
# print(m.groups())
# print(m.group(1))
# print(m.group(2))