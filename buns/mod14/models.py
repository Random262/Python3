import sqlite3

from flask import Flask
from typing import List, Dict


DATA = [
    {'id': 1, 'title': 'A byte of Python', 'author': 'Swaroop C. H.'},
    {'id': 2, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 3, 'title': 'Mar and Peace', 'author': 'Lev Tolstoy'},
]


class Book:
    def __init__(self, title: str, author: str, id: int = None):
        self.id = id
        self.title = title
        self.author = author

    def __getitem__(self, item):
        return getattr(self, item)

    def save(self):
        with sqlite3.connect('table_books.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO table_books (title, author) VALUES (?, ?)',
                (self.title, self.author)
            )



def init_db(initial_records: List[Dict]):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type='table' AND name='table_books';"
        )
        exists = cursor.fetchone()
        # Если таблицы нет, создаем ее и заполняем
        if not exists:
            exists = cursor.executescript(
                """CREATE TABLE IF NOT EXISTS 'table_books' (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT, 
                author TEXT
                )"""
            )
            cursor.executemany(
                'INSERT INTO table_books'
                '(title, author) VALUES (?, ?)',
                [(item['title'], item['author']) for item in initial_records]
                #Делаем записи
            )


def get_all_books() -> List[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * from table_books')
        all_books = cursor.fetchall()
        return [Book(title=row[1], author=row[2], id=row[0]) for row in all_books]
        #Объединяем данные из БД, создаем из кортежа объект нашего класса


def get_books_by_author(author_name: str) -> List[Book]:
    books = []
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM table_books WHERE author=?', (author_name,))
        rows = cursor.fetchall()
        for row in rows:
            book = Book(title=row[1], author=row[2], id=row[0])
            books.append(book)
    return books

if __name__ == '__main__':
    init_db(DATA)


