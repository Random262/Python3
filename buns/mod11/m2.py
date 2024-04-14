import sqlite3
import threading
import time
import requests


def download_sw_chars_seq():
    start = time.time()
    chars = []
    for i in range(18, 38):
        response = requests.get(f"https://swapi.dev/api/people/{i}/")
        data = response.json()
        chars.append((data["name"], data["birth_year"], data["gender"]))

    with sqlite3.connect("sw_char.db") as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS characters ( "
                       "id INTEGER PRIMARY KEY, "
                       "name TEXT, "
                       "birth_year TEXT, "
                       "gender TEXT)")
        cursor.executemany("INSERT INTO characters (name, birth_year, gender) VALUES (?, ?, ?)", chars)
    end = time.time()
    print(f"Downloading took {end - start:.3f} s")


def download_sw_chars_thread():
    start = time.time()
    chars = []

    def download_sw_chars(i):
        response = requests.get(f"https://swapi.dev/api/people/{i}/")
        data = response.json()
        chars.append((data["name"], data["birth_year"], data["gender"]))

    threads = []
    for i in range(18, 38):
        thread = threading.Thread(target=download_sw_chars, args=(i,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    with sqlite3.connect("sw_char.db") as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS characters ( "
                       "id INTEGER PRIMARY KEY, "
                       "name TEXT, "
                       "birth_year TEXT, "
                       "gender TEXT)")
        cursor.executemany("INSERT INTO characters (name, birth_year, gender) VALUES (?, ?, ?)", chars)
    end = time.time()
    print(f"Downloading with treads took {end - start:.3f} s")


def main():
    download_sw_chars_seq()
    download_sw_chars_thread()


if __name__ == "__main__":
    main()