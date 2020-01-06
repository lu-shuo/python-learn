#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'调试'

__author__ = 'Darren Lu'

import logging
LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "#配置输出日志格式
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a ' #配置输出时间的格式，注意月份和天数不要搞乱了
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt = DATE_FORMAT ,
                    filename=r"D:\学习\Python\learn.log" #有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                    )

# 可以直接print()打出要看的变量，但是最后还要删掉，不建议，有以下几种代替方法

# 1. assert,assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。

# 如果断言失败，assert语句本身就会抛出AssertionError：
# def fn(s):
#     n = int(s)
#     assert n != 0,'error'
#     return 10 / n

# 启动Python解释器时可以用-O参数来关闭assert

# 2.logging
# 和assert比，logging不会抛出错误，而且可以输出到文件：
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

