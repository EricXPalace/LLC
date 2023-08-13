import pandas as pd

contact = {
  "name": ["Olivia", "Hamlet", "Lancelot"],
  "court": [301, 505, 212],
  "charge": ["Grand Thaft Auto", "First-degree murder", "bank heist"]
}

framer = pd.DataFrame(contact)

print(framer)
print("=====================================================")
print(framer["name"])
print("=====================================================")
print(framer["name"].count)
print("=====================================================")
print(type(framer["name"]))
print("=====================================================")
print(framer[["name","court"]])
print("=====================================================")
print(framer.columns)
print("=====================================================")
print(framer.iloc[0])
print("=====================================================")
print(framer.loc[301])