import sqlite3




def create_table():
    conn = sqlite3.connect('employers.db')
    cursor = conn.cursor()
    cursor.execute('''  
        CREATE TABLE IF NOT EXISTS task (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            task TEXT
        )
    ''')

    conn.commit()
    conn.close()


def insert_task(user_id, task):
    conn = sqlite3.connect('employers.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO task (user_id, task)
        VALUES (?, ?)
    ''', (user_id, task))

    conn.commit()
    conn.close()


def find_tasks_for_user(user_id):
    conn = sqlite3.connect('employers.db')
    cursor = conn.cursor()

    result = cursor.execute('''
        SELECT task FROM task WHERE user_id = ?
    ''', (user_id,)).fetchall()

    conn.close()

    return result
