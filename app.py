from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = [{"name" : "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "fist-app"},
        {"name": "Обратная связь", "url": "contact"}]

@app.route('/')
def index():
    print( url_for('index'))
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    print( url_for('about'))
    return render_template('about.html', title='О сайте', menu=menu)

@app.route('/contact')
def contact():
    print( url_for('contact'))
    return render_template('contact.html', title='Обратная связь', menu=menu)

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page" + name + '-' + id


@app.route('/profile/<username>')
def profile(username):
    return f"Пользователь: {username}"


# with app.test_request_context(): # тестовый контекст запрос
#     print( url_for('index'))
#     print( url_for('about'))
#     print( url_for('profile', username='denis'))

if __name__ == '__main__':
    app.run(debug=True)
