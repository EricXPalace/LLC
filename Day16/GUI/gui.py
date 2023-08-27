import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import sales_data, annual_sales

fig1,ax1 = plt.subplots()
ax1.bar(sales_data.keys(), sales_data.values())
ax1.set_title("Sales Data")
ax1.set_xlabel("Product")
ax1.set_ylabel("Sales")

fig2,ax2 = plt.subplots()
ax2.bar(annual_sales.keys(), annual_sales.values())
ax2.set_title("Annual Sales")
ax2.set_xlabel("Salesman")
ax2.set_ylabel("Sales")

root = tk.Tk()

root.title("matplotlib")
root.state("normal")

side_frame = tk.Frame(root, bg="#198964")
side_frame.pack(side="left", fill="y")

label = tk.Label(side_frame, text="Dashboard", bg="#aa2525", fg="#FFFFFF", font=25)
label.pack(pady=50,padx=20)

charts_frame = tk.Frame(root)
charts_frame.pack()

upper_fragme = tk.Frame(charts_frame)
upper_fragme.pack(fill="both", expand=True)

canvas1 = FigureCanvasTkAgg(fig1, upper_fragme)
canvas1.draw()
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas2 = FigureCanvasTkAgg(fig1, upper_fragme)
canvas2.draw()
canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

root.mainloop()