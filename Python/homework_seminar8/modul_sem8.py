import sqlite3
import user_interface as us

bd = sqlite3.connect("hw_base.db")
cursor = bd.cursor()

def find_id():
    
    id_num = us.search_id()
    cursor.execute(f'SELECT * FROM personal WHERE id={id_num};')
    one= cursor.fetchone()
    print(*one)
    

def find_last_name():
    last_n = us.search_surname()
    cursor.execute(f'SELECT * FROM  personal WHERE last_name="{last_n}";')
    one= cursor.fetchmany()
    print(*one)
    

def delete_data():
    choice = us.delete_id()
    cursor.execute(f'DELETE FROM personal WHERE id={choice};')
    bd.commit()
    
def update_personal():
    id_sal = us.update_salary()
    cursor.execute(f'UPDATE personal SET salary = {int(id_sal[1])} WHERE id={id_sal[0]};')
    bd.commit()
    
def print_baza():
    for i in cursor.execute('SELECT * FROM personal'):
        print(*i)