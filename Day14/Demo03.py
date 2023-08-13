import pandas as pd
import matplotlib.pyplot as plt

# 定義資料
ages = [18, 42, 50, 19, 37, 26, 55, 32, 19, 22]

# 定義圖表
plt.hist(ages, bins=10, edgecolor="black")

target = 35
plt.axvline(x=target)

# 設定標題
plt.title("A Nasty Stack")

# 調整圖表佈局
plt.tight_layout()

# 顯示圖表
plt.show()