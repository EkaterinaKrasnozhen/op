import sqlite3


bd= sqlite3.connect('Data_base.db')

cursor = bd.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS personal (
    id INTEGER PRIMARY KEY,
    name TEXT,
    last_name TEXT,
    position TEXT,
    salary INT,
    bouns INT
    )''')

baza = [(1,'Иван', 'Иванов', 'главный инженер', 55000, 20000), #json {1: {name: Иван, last_name: Иванов}
        (2,'Ольга', 'Иванова', 'бухгалтер', 60000, 20000),      #    2:{ }}
        (3,'Виктор', 'Петров', 'слесарь', 45000, 15000)]        #import json, dump - in json, load - from json

try:
    cursor.executemany('INSERT INTO personal VALUES(?,?,?,?,?,?)',baza)
    bd.commit()

except:
    print('Данные уже есть')


    
cursor.execute('DELETE FROM personal WHERE id=1;')
bd.commit()
# cursor.execute('SELECT * FROM  personal WHERE last_name LIKE "Иванова";')
# one= cursor.fetchmany()
# print(*one)

# cursor.execute('SELECT * FROM personal WHERE id=3;')
# one= cursor.fetchone()
# print(*one)


        
        
def naprimer():   # сделали заглушку, дальше можно использовать внутри другой функции
    pass


 

# user delete
def delete_from_user():
    us_choice = int(input('Введите номер id для удаления: '))   
    return us_choice

#user search
def search_from_user():
    uschoice_surname = input('Введите номер id для удаления: ')   
    return uschoice_surname

#  model delete
def delete_data():
    choice = delete_from_user()
    cursor.execute(f'DELETE FROM personal WHERE id={choice};')
    bd.commit()

# model search surname   
def find_in_data():
    surname_choice = search_from_user()
    cursor.execute(f'SELECT * FROM  personal WHERE last_name LIKE "{surname_choice}";') #LIKE выдаст несколько если есть
    one= cursor.fetchmany() #fetchall
    return one #return cursor.fetchmany вместо one, ctrl + мышкой посмотреть значения функции

# по кругу для меню
def user_choice():
    while True:
        user_choice = input('1 - посмотреть\n 2 - внести\n q - выход')
        if user_choice == '1':
            naprimer()
        elif user_choice =='2':
            naprimer()
        elif user_choice == 'q':
            print('выход')
            break
        else:
            print('нет такого пункта меню')
            

            
# все функции для меню в modul

cursor.execute('UPDATE personal SET salary = 70000 WHERE id=2;')
bd.commit()
for i in cursor.execute('SELECT * FROM personal'):
        print(*i)
        
# https://www.sqlite.org/docs.html
# https://sqlitestudio.pl/
# https://dbeaver.io/