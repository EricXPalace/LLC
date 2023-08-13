import pandas as pd

contact = {
  "name": ["Olivia Hamson", "Hamlet Conard", "Lancelot R. Berrid", "Dayton Metaphor", "Elizabeth Dayton", "Amerster Dickenson", "Rolling Maphor"],
  "court": [301, 505, 212, 301, 505, 302, 503],
  "charge": ["Grand Thaft Auto", "First-degree murder", "bank heist", "First-degree murder", "Illegal Armed", "Scamming", "Second-degree murder"],
  "case": ["01023698", "22445360", "11025683", "25689432", "11145834", "50026389", "28556931"]
}

def main():

  frame = pd.DataFrame(contact)

  frame.rename(columns={"name":"被告姓名", "court":"法庭號", "charge":"罪名", "case":"備案號"})
  print(frame)

if __name__ == "__main__":
  main()