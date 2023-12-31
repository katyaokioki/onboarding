from flask import Flask, request, render_template

import db

app = Flask(__name__)


@app.route('/')
def hello():
    # return 'Hello, World!'
    return render_template('login.html')

@app.route('/main')
def main():
    return render_template('index.html')


# @app.route('/login')
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         return 'Вы вошли в систему!'
#     else:
#         return render_template('login.html')

    # return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/events')
def events():
    return render_template('events.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    employee = None

    if request.method == 'POST':
        first_name = request.form.get('first_name')
        employee = db.find_by_first_name(str(first_name))

    return render_template('search.html', employee=employee)


if __name__ == '__main__':
    # db.create_table()
    # db.insert_into_table()
    # print(db.find_all())
    app.run()







