from flask import Flask, render_template

app = Flask(__name__)

menu = ["Установка", "Первое приложение", "Обратная связь"]

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='О сайте', menu=menu)


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page" + name + '-' + id


if __name__ == '__main__':
    app.run(debug=True)
