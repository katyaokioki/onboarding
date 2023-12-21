import sqlite3




def create_table():
    conn = sqlite3.connect('employers.db')
    cursor = conn.cursor()
    cursor.execute('''  
        CREATE TABLE IF NOT EXISTS employers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            position TEXT,
            experience TEXT,
            age INTEGER,
            salary INTEGER,
            phone_number INTEGER,
            address TEXT,
            email TEXT
        )
    ''')

    conn.commit()
    conn.close()


def insert_into_table():
    conn = sqlite3.connect('employers.db')
    cursor = conn.cursor()
    cursor.execute('''  
        INSERT INTO employers (
            first_name,
            last_name,
            position,
            experience,
            age,
            salary,
            phone_number,
            address,
            email
        )   
        VALUES ('Савиди', "Юра", "уборщик", "без опыта", 18, 10, 7789546324, "ул. Михалковского,7 к.3", "anapa2005yandex/ru")
    ''')

    conn.commit()
    conn.close()


def find_by_first_name(first_name):
    conn = sqlite3.connect('employers.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * from employers WHERE first_name = ?", (first_name,))

    return cursor.fetchall()


def find_all():
    conn = sqlite3.connect('employers.db')
    cursor = conn.cursor()
    cursor.execute(f'''
         SELECT * from employers WHERE first_name = "Иванов"
     ''')

    return cursor.fetchall()

