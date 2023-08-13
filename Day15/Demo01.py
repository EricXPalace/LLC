import matplotlib.pyplot as plt

# 定義假資料
x = ["Java", "Python", "C", "Rust"]
y = [85.9, 94.1, 99.7, 65.3]
color = ["red", "#cfcf00", "green", "blue"]
edge = ["black", "black", "#c0c0c0", "#c0c0c0"]
y2 = [27.1, 15.3, 39.6, 24.7]

# 繪製柱狀圖
plt.bar(x, y, width=0.2, color=color, edgecolor=edge, alpha=0.75, label=x)
plt.plot(x, y2, color="black", marker=".", label="y2")

# 定義標籤
plt.xlabel("Catagories")
plt.ylabel("Usage")
plt.title("Test Program")
plt.legend(loc="upper right")

# 顯示圖表
plt.show()