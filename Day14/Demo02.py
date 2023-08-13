import matplotlib.pyplot as plt

# 定義資料
minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shard01 = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4]
shard02 = [2, 4, 6, 4, 5, 8, 1, 2, 3, 7]
shard03 = [5, 6, 7, 2, 8, 4, 3, 5, 1, 6]
labels = ["shard01", "shard02", "shard03"]

# 建立堆疊圖
plt.stackplot(minutes, shard01, shard02, shard03, labels=labels)

# 設定標題
plt.title("A Nasty Stack")
plt.legend(loc="upper left")

# 調整圖表佈局
plt.tight_layout()

# 顯示圖表
plt.show()
