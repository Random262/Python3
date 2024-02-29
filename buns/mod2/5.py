from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:numbers>")
def max_number(numbers):
    line = numbers.split('/')
    flag, maxi = False, None
    for num in line:
        if not flag:
            if is_number(num):
                maxi = float(num)
                flag = True
        else:
            if is_number(num):
                temp = float(num)
                if temp > maxi:
                    maxi = temp
    if maxi is not None:
        maxi = int(maxi) if maxi.is_integer() else maxi
        return f"Максимальное переданное число <i>{maxi}</i>"
    else:
        return "Ни одно число не было получено"


def is_number(num):
    try:
        res = float(num)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    app.run(debug=True)
