from flask import Flask
from werkzeug.routing import Rule

app = Flask(__name__)


def available(func):
    def decorated(*args, **kwargs):
        endpoints = [rule.endpoint for rule in app.url_map.iter_rules()][1:]
        for i in app.url_map.iter_rules():
            return func(endpoints)
    return decorated


@app.errorhandler(404)
@available
def page_not_found(endpoints):
    pages = ', '.join(endpoints)
    result = f"The requested URL was not found on the server. Available pages: {pages}."
    return result, 404


@app.route('/')
def home():
    return 'Home'


@app.route('/best')
def best():
    return 'You are the best!'


@app.route('/hello')
def hello():
    return 'Hello, world!'


if __name__ == '__main__':
    app.run(debug=True)
