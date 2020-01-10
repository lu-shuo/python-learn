#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'tkinter'

__author__ = 'Darren Lu'

import tkinter as tk



# width,height以字符宽高为单位
window = tk.Tk()
window.title('my window')
window.geometry('300x300')

# l = tk.Label(window, text='Hello', bg='green', font='Arial,12', width=15, height=2)
# l.pack()

# var = tk.StringVar()
# l = tk.Label(window, textvariable=var, bg='green', font='Arial,12', width=15, height=2)
# l.pack()

# on_click = False
# def onclick():
#     global on_click
#     if on_click == False:
#         on_click = True
#         var.set('hello,world')
#     else:
#         on_click = False
#         var.set('')

# b = tk.Button(window, text='click', command=onclick, width=15, height=2)
# b.pack()

# #输入
# e = tk.Entry(window, show='hah') #show='*'显示样式为*,理论上可以为任意数字
# e.pack()

# def insert_point():
#     var = e.get()
#     t.insert('insert', var)

# def insert_end():
#     var = e.get()
#     t.insert('end', var)
    # 第三种形式，可以指定插入地点，比如insert(1.1, var)是插入在第一行第一列

# b1 = tk.Button(window, text='insert point', width=15, height=2, command=insert_point)
# b2 = tk.Button(window, text='insert end', width=15, height=2, command=insert_end)
# b1.pack()
# b2.pack()
# # 文本框
# t = tk.Text(window, height=2)
# t.pack()






# var1 = tk.StringVar()

# l3 = tk.Label(window, textvariable=var1, bg='yellow', font='Arial,12', width=4, height=2)
# l3.pack()

# def print_selection():
#     value = lb.get(lb.curselection())
#     var1.set(value)

# var2 = tk.StringVar()
# var2.set((11,22,33,44))

# # 下拉框
# lb = tk.Listbox(window, listvariable = var2)
# lb.pack()

# list_item = [1,2,3,4]
# for item in list_item:
#     lb.insert('end', item)
# lb.insert(2, 'second')
# lb.delete(2)
# b3 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
# b3.pack()





var4 = tk.StringVar()
l4 = tk.Label(window, text='empty', bg='yellow', font='Arial,12', width=4, height=2)
l4.pack()
def print_selection_radio():
    # l4.config(text='You have selected' + var4.get())
    l4.config(text=var4.get())
r1 = tk.Radiobutton(window, text='Option A', variable=var4, value='A', command=print_selection_radio)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B', variable=var4, value='B', command=print_selection_radio)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C', variable=var4, value='C', command=print_selection_radio)
r3.pack()
window.mainloop()