import matplotlib.pyplot as plt
import numpy as np

# 定義假資料
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
color = ["b", "g", "r", "c", "m", "y", "k", "w", "#c0c0c0", "#198964"]

# 定義顏色等等美術細節


# 繪製柱狀圖
plt.scatter(x, y, label="Some scatter dots", c=color)

# 定義標籤
plt.xlabel("X-line")
plt.xticks(rotation=45)
plt.ylabel("Y-line")
plt.title("Title")


# 顯示圖表
plt.legend(loc = "upper right")
plt.show()