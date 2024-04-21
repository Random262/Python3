import sqlite3
import time
import requests
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool


def download_sw_char(i):
    response = requests.get(f"https://swapi.dev/api/people/{i}/")
    data = response.json()
    return (data["name"], data["birth_year"], data["gender"])

def download_sw_chars_pool():
    start = time.time()

    with Pool() as pool:
        chars = pool.map(download_sw_char, range(18, 38))

    with sqlite3.connect("sw_char.db") as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS characters ( "
                       "id INTEGER PRIMARY KEY, "
                       "name TEXT, "
                       "birth_year TEXT, "
                       "gender TEXT)")
        cursor.executemany("INSERT INTO characters (name, birth_year, gender) VALUES (?, ?, ?)", chars)

    end = time.time()
    print(f"Downloading with Pool took {end - start:.3f} s")


def download_sw_chars_thread_pool():
    start = time.time()

    with ThreadPool() as pool:
        chars = pool.map(download_sw_char, range(18, 38))

    with sqlite3.connect("sw_char.db") as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS characters ( "
                       "id INTEGER PRIMARY KEY, "
                       "name TEXT, "
                       "birth_year TEXT, "
                       "gender TEXT)")
        cursor.executemany("INSERT INTO characters (name, birth_year, gender) VALUES (?, ?, ?)", chars)

    end = time.time()
    print(f"Downloading with ThreadPool took {end - start:.3f} s")


def main():
    download_sw_chars_pool()
    download_sw_chars_thread_pool()


if __name__ == "__main__":
    main()