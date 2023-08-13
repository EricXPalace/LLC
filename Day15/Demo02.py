import matplotlib.pyplot as plt
import numpy as np

# 定義假資料
x = ["Java", "Python", "C", "Rust"]
y = [85.9, 94.1, 99.7, 65.3]

# 定義顏色等等美術細節
color = ["red", "#cfcf00", "green", "blue"]
color2 = ["#e0d216", "#198964", "#2335c7", "#ee3535"]
edge = ["black", "black", "#c0c0c0", "#c0c0c0"]
y2 = [27.1, 15.3, 39.6, 24.7]
w = 0.2

# 繪製柱狀圖
p = np.arange(len(x))
p1 = [j + w for j in p]

plt.bar(x, y, width=w, color=color, edgecolor=edge, alpha=0.75, label=x)
plt.bar(x, y2, width=w, color=color2, label="y2")

# 定義標籤
plt.xlabel("Catagories")
plt.ylabel("Usage")
plt.title("Test Program")
plt.legend(loc="upper right")

# 顯示圖表
plt.show()