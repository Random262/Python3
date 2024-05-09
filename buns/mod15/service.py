# service.py
import sqlite3

DB_FILE = 'hotel.db'


def get_rooms(check_in_date, check_out_date, guests_num):
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute('''SELECT roomId, floor, beds, guest_num, price FROM rooms WHERE guest_num >= ?''', (guests_num,))

        rows = cur.fetchall()
        rooms = []
        for row in rows:
            room = {
                "roomId": row[0],
                "floor": row[1],
                "guestNum": row[3],
                "beds": row[2],
                "price": row[4]
            }
            rooms.append(room)
        return rooms


def add_room(floor, beds, guest_num, price):
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute('''INSERT INTO rooms(floor, beds, guest_num, price)
                       VALUES(?,?,?,?)''', (floor, beds, guest_num, price))
        conn.commit()


def book_room(room_id):
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute('''SELECT * FROM rooms WHERE roomId=?''', (room_id,))
        room = cur.fetchone()
        if room is None:
            return False
        cur.execute('''DELETE FROM rooms WHERE roomId=?''', (room_id,))
        conn.commit()
        return True
