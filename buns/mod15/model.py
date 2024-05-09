import sqlite3

DB_FILE = 'hotel.db'


def create_table():
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS rooms (
                            roomId INTEGER PRIMARY KEY,
                            floor INTEGER NOT NULL,
                            beds INTEGER NOT NULL,
                            guest_num INTEGER NOT NULL,
                            price INTEGER NOT NULL
                        );''')


def create_room(room):
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute('''INSERT INTO rooms(floor, beds, guest_num, price)
                       VALUES(?,?,?,?)''', room)
        return cur.lastrowid


def initialize_database():
    create_table()
    rooms = [
        (2, 1, 2, 2000),
        (1, 1, 2, 2500)
    ]
    for i in range(5):
        for room in rooms:
            create_room(room)

