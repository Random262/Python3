import re
import sqlite3
from forms import MyForm
from flask import Flask, render_template, request, redirect, url_for
from typing import List, Dict

from models import init_db, DATA, get_all_books, Book, get_books_by_author

app = Flask(__name__)

# BOOKS = [
#     {'id': 0, 'title': 'A byte of Python', 'author': 'Swaroop C. H.'},
#     {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
#     {'id': 2, 'title': 'Mar and Peace', 'author': 'Lev Tolstoy'},
# ]


def _get_hmtl_table_for_books(books: List[Dict]) -> str:
    table = """
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Title</th>
                    <th>Author</th>
                </tr>
            </thead>
                <tbody>
                    {books_rows}
                </tbody>
        </table>
    """
    rows = ''
    for book in books:
        rows += '<tr><td>{id}</td><td>{title}</td><td>{author}</td></tr>'.format(
            id=book['id'], title=book['title'], author=book['author'],
        )
    return table.format(books_rows=rows)


@app.route('/books')
def all_books() -> str:
    return render_template('pred_index.html', books=get_all_books())


@app.route('/books/form', methods=['GET', 'POST'])
def get_books_form():
    form = MyForm()
    if request.method == 'POST':

        if form.validate_on_submit():
            title = form.title.data
            author = form.author.data
            new_book = Book(title=title, author=author)
            new_book.save()

    return render_template('add_book.html', form=form)

@app.route('/books/author', methods=['GET', 'POST'])
def get_books_by_author_page():
    if request.method == 'POST':
        author_name = request.form['author_name']
        books = get_books_by_author(author_name)
        return render_template('books_by_author.html', author=author_name, books=books)
    return render_template('get_books_by_author.html')


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
