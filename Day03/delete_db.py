import sqlite3
from create_db import *
from search_db import *
from update_db import *

with sqlite3.connect("demo_db.db") as db:

    def delete_db():
        db.execute('DELETE FROM Student WHERE id = 2')

        db.commit()

    def main():
        delete_db()

if __name__ == "__main__":
    main()