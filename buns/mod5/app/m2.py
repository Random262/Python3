import signal
from subprocess import Popen, PIPE, TimeoutExpired
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)


class PythonCodeForm(FlaskForm):
    code = StringField(validators=[InputRequired(message="Питон код не введен")])
    timeout = IntegerField(validators=[InputRequired(message="Введите таймаут до 30"),
                                       NumberRange(min=0, max=30, message="Введите число от 0 до 30")])


@app.route('/run', methods=['POST'])
def run():
    global process
    form = PythonCodeForm()
    if form.validate_on_submit():
        code, timeout = form.code.data, form.timeout.data
        if 'shell=True' in code:
            return 'Недопустимый код'
        try:
            process = Popen(['prlimit', '--nproc=1:1', 'python3', '-c', code],
                            stdout=PIPE, stderr=PIPE, preexec_fn=lambda: signal.alarm(timeout))
            outs, errs = process.communicate(timeout=timeout)
        except TimeoutExpired:
            process.kill()
            outs, errs = process.communicate()
            return outs.decode('utf-8') + '\nПревышено время работы программы', 400
        except Exception as e:
            return str(e), 400

        if process.returncode == 0:
            return outs.decode('utf-8')
        elif process.returncode == -14:
            outs, errs = process.communicate()
            return outs.decode('utf-8') + '\nПревышено время работы программы', 400
        else:
            return errs.decode('utf-8') + f'\nВозникла ошибка {process.returncode}', 400
    return f'Неправильный ввод, {form.errors}', 400


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)


