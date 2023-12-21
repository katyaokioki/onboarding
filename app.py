from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
    # return render_template('index.html')


@app.route('/about')
def about():
    return 'Здесь будет информация об авторе сайта.'


@app.route('/blog')
def blog():
    return 'Это блог с заметками о работе и увлечениях.'


@app.route('/login')
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return 'Вы вошли в систему!'
    else:
        return render_template('login.html')

    # return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/map')
def map():
    return render_template('map.html')


if __name__ == '__main__':
    app.run()







