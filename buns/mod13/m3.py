import datetime
import sqlite3


import sqlite3


def create_birds_table(conn):
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS birds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bird_name TEXT NOT NULL,
        observation_date TEXT NOT NULL
    );
    """)
    conn.commit()


def log_bird(c: sqlite3.Cursor,
             bird_name: str,
             date_time: str) -> None:
    c.execute("""
        INSERT INTO birds (bird_name, observation_date) VALUES (?, ?);
        """, (bird_name, date_time))


def check_if_such_bird_already_seen(c: sqlite3.Cursor,
                                    bird_name: str) -> bool:
    c.execute("""
        SELECT EXISTS (SELECT 1 FROM birds WHERE bird_name = ?);
        """, (bird_name,))
    return c.fetchone()[0]


if __name__ == "__main__":
    print("Программа помощи ЮНатам v0.1")
    name = input("Пожалуйста введите имя птицы\n> ")
    count_str = input("Сколько птиц вы увидели?\n> ")
    count = int(count_str)
    right_now = str(datetime.datetime.now(datetime.UTC))

    with sqlite3.connect("hw.db") as connection:
        create_birds_table(connection)
        cursor = connection.cursor()
        if check_if_such_bird_already_seen(cursor, name):
            print("Такую птицу мы уже наблюдали!")
        log_bird(cursor, name, right_now)
        connection.commit()


