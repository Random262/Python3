import json

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, Field, ValidationError
from wtforms.validators import InputRequired, Email, NumberRange, Optional
from flask import Flask, request

app = Flask(__name__)


def number_length(min_len: int, max_len: int, message: str = None):
    def _number_length(form: FlaskForm, field: Field):
        number = field.data
        str_number = str(number)
        if len(str_number) < min_len or len(str_number) > max_len or number < 0:
            if message:
                raise ValidationError(message)
            else:
                raise ValidationError(f"Число должно содержать от {min_len} до {max_len} цифр и быть положительным")

    return _number_length

class NumberLength:
    def __init__(self, min_len: int, max_len: int, message: str = None):
        self.min_len = min_len
        self.max_len = max_len
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        number = field.data
        str_number = str(number)
        if len(str_number) < self.min_len or len(str_number) > self.max_len or number < 0:
            if self.message:
                raise ValidationError(self.message)
            else:
                raise ValidationError(
                    f"Число должно содержать от {self.min_len} до {self.max_len} цифр и быть положительным")


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(message="Email введен не верно"),
                                    Email(message="Email введен не верно")])
    phone1 = IntegerField(validators=[InputRequired(message="Введите числовую последовательность"),
                                      number_length(10, 10)])
    phone2 = IntegerField(validators=[InputRequired(message="Введите числовую последовательность"),
                                      NumberLength(10, 10, message="Должно быть 10 цифр")])
    name = StringField(validators=[InputRequired(message="Имя введено не верно")])
    address = StringField(validators=[InputRequired(message="Адрес введен не верно")])
    index = IntegerField(validators=[InputRequired(message="Индекс введен не верно")])
    comment = StringField(validators=[Optional()])


@app.route('/registration', methods=['POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        email, phone1, phone2 = form.email.data, form.phone1.data, form.phone2.data

        return f"Пользователь {email} успешно зарегистрирован, первый номер телефона +7{phone1}, резервный номер +7{phone2}"
    errors_list = form.errors
    print(errors_list)
    return f"Неправильный ввод, {form.errors}", 400


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
