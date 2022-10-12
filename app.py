from flask import Flask, render_template, request, flash, url_for, session, redirect, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jlsdfghusr'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

# class Article(db.Model):
#     id = db.Column(db.Integer, primery_key=True)
#     title = db.Column(db.String(100), nullabale=False)
#     intro = db.Column(db.String(300), nullabel=False)
#     text = db.Column(db.Text, nullabel=False)
#     date = db.Column(db.Datetime, default=datetime.utcnow)

menu = [{"title" : "Установка", "url": "install-flask"},
        {"title": "Первое приложение", "url": "fist-app"},
        {"title": "Обратная связь", "url": "contact"}]

@app.route('/')
def index():
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='О сайте', menu=menu)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')

    return render_template('contact.html', title='Обратная связь', menu=menu)

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page" + name + '-' + id

# @app.route('/profile/<username>')
# def profile(username):
#     return f"Пользователь: {username}"


# with app.test_request_context(): # тестовый контекст запрос
#     print( url_for('index'))
#     print( url_for('about'))
#     print( url_for('profile', username='denis'))

@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogger' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "densparrow" and request.form['psw'] == "123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title="Авторизация", menu=menu)

@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)

    return f"Профиль пользователя: {username}"

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', tittle="Страница не найдена", menu=menu), 404


if __name__ == '__main__':
    app.run(debug=True)
