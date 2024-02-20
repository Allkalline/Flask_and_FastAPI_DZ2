from flask import Flask, render_template, request, flash, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = 'd04a3aca787b0a0dde54bb39c3a420dbb3ff2c83452ac7373c1c6e4cb5b49925'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# Задание №4
# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.


@app.route('/task4', methods=['GET', 'POST'])
def task4():
    if request.method == 'POST':
        text = request.form.get('text')
        words = len(text.split())
        return render_template('result_for_task4.html', words=words)
    return render_template('task4.html')


# Задание №5
# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.

@app.route('/task5', methods=['GET', 'POST'])
def task5():
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        operation = request.form.get('operation')
        result = None
        if operation == '+':
            result = int(num1) + int(num2)
        elif operation == '-':
            result = int(num1) - int(num2)
        elif operation == '*':
            result = int(num1) * int(num2)
        elif operation == '/':
            result = int(num1) / int(num2)
        return render_template('result_for_task5.html', result=result, num1=num1, num2=num2, operation=operation)
    return render_template('task5.html')


# Задание №6
# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.


@app.route('/task6', methods=['GET', 'POST'])
def task6():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        if int(age) < 0 or int(age) > 125:
            return render_template('error_for_task6.html', name=name.capitalize(), age=age)
        else:
            return render_template('result_for_task6.html', name=name.capitalize(), age=age)
    return render_template('task6.html')


# Задание №7
# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.


@app.route('/task7', methods=['GET', 'POST'])
def task7():
    if request.method == 'POST':
        num = request.form.get('num')
        square = int(num) ** 2
        return render_template('result_for_task7.html', num=num, square=square)
    return render_template('task7.html')


# Задание №8
# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".

@app.route('/task8', methods=['GET', 'POST'])
def task8():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Привет, {name}!', category='success')
        return redirect(url_for('task8'))
    return render_template('task8.html')


# Задание №9
# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан cookie файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.


@app.route('/task9', methods=['GET', 'POST'])
def task9():
    return render_template('task9.html')


@app.route('/welcome', methods=['POST'])
def welcome():
    name = request.form.get('name')
    email = request.form.get('email')

    resp = make_response(redirect('/greet'))
    resp.set_cookie('user_data', f'{name}:{email}')
    return resp


@app.route('/greet')
def greet():
    user_data = request.cookies.get('user_data')
    if not user_data:
        return redirect('/')

    name, _ = user_data.split(':')
    return render_template('greet.html', name=name)


@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('user_data', '', expires=0)
    return resp


if __name__ == '__main__':
    app.run(debug=True)
