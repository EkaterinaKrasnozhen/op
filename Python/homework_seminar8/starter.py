import sqlite3


def create_data_baze():
    bd = sqlite3.connect("hw_base.db")

    cursor = bd.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS personal (
    id INTEGER PRIMARY KEY,
    name TEXT,
    last_name TEXT,
    position TEXT,
    salary INT,
    mobile TEXT
    )""")

    baza = [(1, "Иван", "Иванов", "главный инженер", 55000, 89262264243),
        (2, "Ольга", "Иванова", "бухгалтер", 60000, 89786753434),
        (3, "Виктор", "Петров", "слесарь", 45000, 89285676554),]
    
    try:
      cursor.executemany('INSERT INTO personal VALUES(?,?,?,?,?,?)',baza)
      bd.commit()
    except:
      print('Данные уже есть')

create_data_baze()


    