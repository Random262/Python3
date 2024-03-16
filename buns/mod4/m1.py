from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, NumberRange, Optional
from flask import Flask

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(message="Email введен не верно"), Email(message="Email введен не верно")])
    phone = IntegerField(validators=[InputRequired(message="Введите числовую последовательность"),
                                     NumberRange(min=1000000000, max=9999999999, message="Должно быть 10 цифр")])
    name = StringField(validators=[InputRequired(message="Имя введено не верно")])
    address = StringField(validators=[InputRequired(message="Адрес введен не верно")])
    index = IntegerField(validators=[InputRequired(message="Индекс введен не верно")])
    comment = StringField(validators=[Optional()])


@app.route('/registration', methods=['POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Пользователь {email} успешно зарегистрирован с номером телефона +7{phone}"
    errors_list = form.errors
    print(errors_list)
    return f"Неправильный ввод, {form.errors}", 400


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
