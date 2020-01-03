#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'使用枚举类'

__author__ = 'Darren Lu'

# 起步

# Python 的原生类型中并不包含枚举类型。为了提供更好的解决方案，Python 通过 PEP 435 在 3.4 版本中添加了 enum 标准库。
# 枚举类型可以看作是一种标签或是一系列常量的集合，通常用于表示某些特定的有限集合，例如星期、月份、状态等。在没有专门提供枚举类型的时候我们是怎么做呢，一般就通过字典或类来实现：
# Color = {
#     'RED'  : 1,
#     'GREEN': 2,
#     'BLUE' : 3,
# }

# class Color:
#     RED   = 1
#     GREEN = 2
#     BLUE  = 3

# print(Color)

# 这种来实现枚举如果小心翼翼地使用当然没什么问题，毕竟是一种妥协的解决方案。它的隐患在于可以被修改。



# 使用 Enum
# 更好的方式是使用标准库提供的 Enum 类型，官方库值得信赖。
from enum import Enum,unique,IntEnum

# class Color(Enum):
#     red = 1
#     green = 2
#     blue = 3

# 枚举成员有值（默认可重复），枚举成员具有友好的字符串表示：
# print(Color.red)
# print(repr(Color.red))
# print(type(Color.red))
# print(Color)
# print(isinstance(Color.red, Color))

# 枚举类型不可实例化，不可更改



# 定义枚举

# 定义枚举时，成员名不允许重复
# class Color(Enum):
#     red = 1
#     green = 2
#     red = 3    # TypeError: Attempted to reuse key: 'red'

# 成员值允许相同，第二个成员的名称被视作第一个成员的别名
# class Color(Enum):
#     red   = 1
#     green = 2
#     blue  = 1

# print(Color.red)              # Color.red
# print(Color.blue)             # Color.red
# print(Color.red is Color.blue)# True
# print(Color(1))               # Color.red  在通过值获取枚举成员时，只能获取到第一个成员

# 若要不能定义相同的成员值，可以通过 unique 装饰
# @unique
# class Color(Enum):
#     red   = 1
#     green = 2
#     blue  = 1  # ValueError: duplicate values found in <enum 'Color'>: blue -> red



# 枚举取值

# 可以通过成员名来获取成员也可以通过成员值来获取成员:
class Color(Enum):
    red = 1
    green = 2
    blue = 3

# print(Color['red'])
# print(Color(1))

# 每个成员都有名称属性和值属性：
member = Color.red
print(member)
print(member.name)
print(member.value)

# 支持迭代的方式遍历成员，按定义的顺序，如果有值重复的成员，只获取重复的第一个成员：
for color in Color:
    print(color)

# 特殊属性 __members__ 是一个将名称映射到成员的有序字典，也可以通过它来完成遍历：
for color in Color.__members__.items():
    print(color)


# 枚举比较

# 枚举的成员可以通过 is 同一性比较或通过 == 等值比较：
print(Color.red is Color.red)
print(Color.red is Color.blue)
print(Color.blue == Color.red)
print(Color.blue != Color.red)

# 枚举成员不能进行大小比较：
# print(Color.red < Color.blue)  #报错



# 扩展枚举 IntEnum
# IntEnum 是 Enum 的扩展，不同类型的整数枚举也可以相互比较：
class Shape(IntEnum):
    circle = 1
    square = 2

class Request(IntEnum):
    post = 1
    get = 2

print(Shape.circle == 1)            # True
print(Shape.circle < 3)             # True
print(Shape.circle == Request.post) # True
print(Shape.circle >= Request.post) # True

