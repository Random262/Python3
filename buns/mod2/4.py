from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/hello-world/<username>")
def hello_world(username):
    today = datetime.today().weekday()
    weekday = weekdays_tuple[today]
    good = 'Хорошей' if today in [2, 4, 5] else 'Хорошего'
    print(good, weekday)
    return f"Привет, {username}. {good} {weekday}!"


weekdays_tuple = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья')

if __name__ == "__main__":
    app.run(debug=True)
