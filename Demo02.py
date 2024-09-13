"""
在文本框中输入圆的面积，输入后点击"计算"按钮即可计算出该圆的周长和面积，要求如下：
【1】圆周率π值取3.1415926
【2】如果输入的是负数、空值或零，提示半径不能负数、空值或零
【3】计算机的结果保留两位小数
"""
from tkinter import *
from tkinter.messagebox import *


class Calculator:
    def __init__(self):  # 初始化gui界面
        self.frame = Tk()  # 创建窗口
        self.frame.title("计算圆的周长和面积")  # 添加窗口标题
        # 指定窗口大小
        self.frame.geometry("600x300")
        # 不允许改变窗体大小
        self.frame.resizable(0, 0)
        # 指定窗体颜色
        self.frame["bg"] = "lightgray"
        # 添加标签
        self.Label_input = Label(self.frame, text="请输入圆的半径：", bg="lightgray", fg="black", font=("宋体", 14, "bold"))
        # 添加标签位置
        self.Label_input.place(x=50, y=50)
        # 添加一个输入的文本框
        self.var_radius = StringVar()
        self.Entry_input = Entry(self.frame, textvariable=self.var_radius, font=("宋体", 14, "bold"), width=30)
        self.Entry_input.place(x=180, y=50)
        # 添加一个计算按钮
        self.Button_cal = Button(self.frame, text="计算", font=("宋体", 14, "bold"), bg="white", width=8, command=self.get_result)
        self.Button_cal.place(x=500, y=52)
        # 圆的周长label
        self.Label_perimeter = Label(self.frame, text="圆的周长：", bg="lightgray", fg="blue", font=("宋体", 14, "bold"))
        self.Label_perimeter.place(x=95, y=110)
        self.Label_perimeter_result = Label(self.frame, text="圆的周长的结果", bg="lightgray", fg="red",
                                            font=("宋体", 14, "bold"))
        self.Label_perimeter_result.place(x=200, y=110)
        # 圆的面积label
        self.Label_area = Label(self.frame, text="圆的面积：", bg="lightgray", fg="blue", font=("宋体", 14, "bold"))
        self.Label_area.place(x=95, y=150)
        self.Label_area_result = Label(self.frame, text="圆的面积的结果", bg="lightgray", fg="red", font=("宋体", 14, "bold"))
        self.Label_area_result.place(x=200, y=150)

    def show(self): # 展示窗体
        self.frame.mainloop()
    def get_result(self):
        radius = float(self.var_radius.get())
        π = 3.1415926
        self.Label_perimeter_result["text"] = ("%.2f" % (2*π*radius))
        self.Label_area_result["text"] = ("%.2f" % (π*radius*radius))


if __name__ == "__main__":  # 主函数
    # 根据类实例化一个对象
    this_gui = Calculator()
    # 展示窗体
    this_gui.show()

