import sqlite3

def main():
    with sqlite3.connect("create_db.db") as db:
        db.execute('\
                           CREATE TABLE if not exists \
                           Student (\
                           id integer NOT NULL PRIMARY KEY AUTOINCREMENT,\
                           name text NOT NULL,\
                           age smallint NOT NULL)\
                           ')
        
        db.execute('''
            INSERT INTO 
            Student(name, age)
            VALUES("Brian Rocksmith", 23)        
        ''')

        db.commit()

if __name__ == "__main__":
    main()