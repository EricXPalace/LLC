import sqlite3
from create_db import *

with sqlite3.connect("demo_db.db") as db:

    def search_db(where = "*"):
        data = db.execute('SELECT * FROM Student WHERE ?', (where))
        
        for record in data:
            print("===================")
            print(f"ID: {record[0]}")
            print(f"Name: {record[1]}")
            print(f"Age: {record[2]}")
            print(f"Stars: {record[3]}")

        db.commit()

    def main():
        search_db("id = 5")

if __name__ == "__main__":
    main()