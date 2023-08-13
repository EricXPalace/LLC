import pandas as pd
import matplotlib.pyplot as plt
import csv

country_name = {"usa": "United States",
               "tw": "Taiwan",
               "jp": "Japan",
               "hk": "Hong Kong"}

file = pd.read_csv("coding/Day14/play.csv")
if print(file) != ():
  for countries in file:
    if countries != "year":
      plt.plot(file.year, file[countries], label=country_name[countries], marker=".")

  plt.legend(loc="upper right")
  plt.xlabel("Year")
  plt.ylabel("Sale")
  plt.title("Annual Sale Rank")
  
  plt.show()

