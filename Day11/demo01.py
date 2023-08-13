import pandas as pd

csvfile = pd.read_csv("coding/html_file/Files/credit_locations.csv")

print(csvfile)
print("==================================")
print(csvfile.shape)
print("==================================")
print(csvfile.info)
print("==================================")
print(csvfile.head)
print("==================================")
print(csvfile.tail)