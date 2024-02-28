import datetime
import os
import random
import re

from flask import Flask

app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'


@app.route('/cars')
def cars():
    global cars_arr
    return ', '.join(cars_arr)


@app.route('/cats')
def cats():
    global cats_arr
    return random.choice(cats_arr)


@app.route('/get_time/now')
def time_now():
    date = datetime.datetime.now()
    return "Точное время: {}".format(date)


@app.route('/get_time/future')
def time_future():
    date = datetime.datetime.now()+datetime.timedelta(hours=1)
    return "Точное время через час будет {}".format(date)


@app.route('/get_random_word')
def get_random_word():
    global words_arr
    return random.choice(words_arr)


def extract_words(file_path):
    result = []
    with open(file_path, 'r', encoding='utf-8') as book:
        for line in book:
            words = line.split()
            for word in words:
                clean_word = re.sub(r'[^\w\s\']', '', word)
                if clean_word:
                    result.append(clean_word)
    return result


@app.route('/counter')
def count():
    global enter_counter
    enter_counter += 1
    return str(enter_counter)


cars_arr = ['Chevrolet', 'Renault', 'Ford', 'Lada']

cats_arr = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')
words_arr = extract_words(BOOK_FILE)

enter_counter = 0
