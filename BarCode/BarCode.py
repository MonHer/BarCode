# -*- encoding: utf-8 -*-
"""
@File    : BarCode.py
@Time    : 2021/5/11 18:18
@Author  : Yuye
@Email   : kpl1888@163.com
@Software: PyCharm
"""

from tkinter import *  # 导入 Tkinter 库
import barcode
from barcode.writer import ImageWriter
from PIL import ImageTk

def create_barcode(code):
    if not code.get():
        return
    CODE128 = barcode.get_barcode_class('code128')
    bar_code = CODE128(code.get(), writer=ImageWriter())
    bar_photo = ImageTk.PhotoImage(bar_code.render())
    imgLabel.config(image=bar_photo)
    imgLabel.image = bar_photo



if __name__ == "__main__":
    root = Tk()  # 创建窗口对象的背景色
    root.title('条形码生成器')
    root.geometry('800x400')
    enter_code = StringVar()
    bar_code_input = Entry(root, textvariable=enter_code)
    bar_code_input.pack()
    btn = Button(root, text='确认', command=lambda: create_barcode(enter_code))
    btn.pack()
    imgLabel = Label(root)
    imgLabel.pack()
    # 进入消息循环
    root.mainloop()