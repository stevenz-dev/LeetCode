import tkinter as tk
import time

# 创建一个 Tkinter 窗口
root = tk.Tk()

# 创建一个标签，显示箭头
label = tk.Label(root, text="↑")
label.pack()

def move_arrow():
    for i in range(5):
        # 更新标签的内容，添加一个空格使箭头向右移动
        label['text'] = " " + label['text']

        # 更新窗口
        root.update()

        # 每秒移动一次
        time.sleep(1)

# 在新的线程中运行动画，防止窗口冻结
root.after(0, move_arrow)

# 运行 Tkinter 事件循环
root.mainloop()
