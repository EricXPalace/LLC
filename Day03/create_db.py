import sqlite3

with sqlite3.connect("demo_db.db") as db:

    def add_db(slot_name, slot_age, slot_stars):
        db.execute('''
            INSERT INTO 
            Student(name, age, stars)
            VALUES(?,?,?)                    
            ''',(slot_name, slot_age, slot_stars))

        db.commit()

    def main():        
        db.execute('''
                CREATE TABLE if not exists 
                Student (
                id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                name text NOT NULL,
                age integer NOT NULL,
                stars smallint NOT NULL)
                ''')
            
        add_db("Arron Kier", 31, 1)
        add_db("Branden Oven", 26, 3)
        add_db("Casedy Rondoll", 40, 4)
        add_db("Diana Guan", 23, 5)
        add_db("Englier Chrome", 27, 3)
        add_db("Fiona Rocksmith", 20, 0)

if __name__ == "__main__":
    main()