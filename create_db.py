import sqlite3

def main():
    with sqlite3.connect("create_db.db") as db:
        db.execute('\
                           CREATE TABLE if not exist \
                           Student (\
                           id integer NOT NULL PRIMARY KEY AUTOINCREMENT,\
                           name text NOT NULL,\
                           age smallint NOT NULL)\
                           ')

if __name__ == "__main__":
    main()