import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

root = tk.Tk()
root.minsize(width=300, height=200)
root.maxsize(width=600, height=400)

# 建立按鈕
button = ttk.Button(root, text="Show Chart")

# 建立圖紙
canvas = tk.Canvas(root, width=500, height=500)

# 在按鈕上綁定事件處理函式
def show_chart():
    # 繪製圖表
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
    ax.set_title("This is a chart")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # 隱藏標頭列
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # 繪製圖表到圖紙上
    canvas.create_image(250, 250, image=plt.gcf().canvas.tostring_rgb())

button.config(command=show_chart)

# 設定視窗主色調
root.configure(background="black")

# 在需要高量提示的部分使用黃色或橘色等進行高光提示
button.config(foreground="yellow").pack()
canvas.config(background="orange").pack()

# 顯示視窗
root.mainloop()