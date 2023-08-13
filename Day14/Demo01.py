import matplotlib.pyplot as plt

slices = [1, 2, 3, 4, 5]
labels = ["A", "B", "C", "D", "E"]
colors = ["blue", "green", "Yellow", "red", "#00e8ca"]
explode = [0, 0, 0, 0, 0.3]

plt.pie(slices, labels=labels, colors=colors, explode=explode, shadow=True, startangle=60, autopct="%1.1f%%")
plt.title("Chart Image")
plt.tight_layout

plt.show()