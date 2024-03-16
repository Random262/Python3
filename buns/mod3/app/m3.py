from flask import Flask

app = Flask(__name__)


@app.route("/add/<date>/<int:number>")
def add(date, number):
    if len(date) > 8 or not date.isdigit():
        raise TypeError("Incorrect date")
    year, month, day = int(date[:4]), int(date[4:6]), int(date[6:8])
    storage.setdefault(year, [0, {}])[0] += number
    storage[year][1].setdefault(month, [0, {}])[0] += number
    storage[year][1][month][1][day] = number
    return 'Data accepted'


@app.route("/calculate/<int:year>")
def calculate_year_fin(year):
    if len(str(year)) > 4 or year < 1:
        raise TypeError("Incorrect date")
    if year not in storage:
        return f'Data for {year} year not entered'
    return f'In the {year} year spent {storage[year][0]}'


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month_fin(year, month):
    if len(str(year)) > 4 or len(str(month)) > 2 or year < 1 or month < 1:
        raise TypeError("Incorrect date")
    if year not in storage:
        return f'Data for {year} year not entered'
    if month not in storage[year][1]:
        return f'Data for {month} month has not been entered'
    return f'In {month} month spent {storage[year][1][month][0]}'


storage = {}

if __name__ == "__main__":
    app.run(debug=True)