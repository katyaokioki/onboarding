from flask import Flask, request, render_template

import db, db1

app = Flask(__name__)

app.template_folder = 'static'


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

        employee_with_tasks = []
        for emp in employee:
            tasks = db1.find_tasks_for_user(emp[0])
            emp += tuple(zip(*tasks))
            employee_with_tasks.append(emp)

        employee = employee_with_tasks

    return render_template('search.html', employee=employee)


if __name__ == '__main__':
    app.run()







