import sqlite3
from create_db import *
from search_db import *

with sqlite3.connect("demo_db.db") as db:

    def update_db(id, name):
        db.execute('UPDATE Student SET name = ? WHERE id = ?',(name, id))

        db.commit()

    def main():
        update_db(2, "Beta Ericsson")

if __name__ == "__main__":
    main()