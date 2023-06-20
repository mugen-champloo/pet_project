import psycopg2
import datetime
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


connection = psycopg2.connect(user="postgres",
                                # пароль, который указали при установке PostgreSQL
                                password="1",
                                host="127.0.0.1",
                                port="5432",
                                database = 'mugen')

cursor = connection.cursor()


# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# cursor = connection.cursor()
# sql_create_database = 'create database mugen'
# cursor.execute(sql_create_database)


# create_table_query = '''CREATE TABLE for_telebot 
                        # (ID INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
                        # Date date,
                        # Name varchar,
                        # Machine varchar,
                        # Other varchar,
                        # Expense int NOT NULL,
                        # Earn int
                        # ); '''
# cursor.execute(create_table_query)
# connection.commit()

def add_expenses(exp):
    cursor.execute('''INSERT INTO for_telebot (date, Name, Machine, Other, Expense, Earn) VALUES (%s, %s, %s, %s, %s, %s)''', exp)
    connection.commit()
    

def delete_data(id):
    cursor.execute("SELECT * from for_telebot WHERE ID=%s", id)
    print_data = cursor.fetchall()

    cursor.execute("DELETE FROM scores WHERE ID=%s", id)
    connection.commit()

    return f'Удалил данные: {print_data}'

def alldata():

    cursor.execute('''SELECT date, name, machine, other, expense, earn from for_telebot;''')
    all_data = cursor.fetchall()

    return all_data

def sum_for_print():
    cursor.execute('''select SUM(Expense) from for_telebot''')
    summa = cursor.fetchall()
    return f'Сумма:  {summa[0][0]}'

def sum():
    cursor.execute('''select SUM(Expense) from for_telebot''')
    summa = cursor.fetchall()
    return summa

def earn_sum_for_print():
    cursor.execute('''select SUM(Earn) from for_telebot''')
    summa = cursor.fetchall()
    return f'Сумма:  {summa[0][0]}'

def earn_sum():
    cursor.execute('''select SUM(Earn) from for_telebot''')
    summa = cursor.fetchall()
    return summa

def last_data():

    cursor.execute("SELECT * FROM for_telebot ORDER BY ID DESC LIMIT 1")
    last_row = cursor.fetchone()
    return last_row

def delete_last_data():
    last_insert = last_data()
    cursor.execute("DELETE FROM for_telebot WHERE id = %s", [last_insert[0]])
    connection.commit()

def specific_data_id(id):
    cursor.execute("SELECT * FROM for_telebot WHERE ID=%s", [id])
    specific_data = cursor.fetchone()
    return specific_data

def delete_specific_data(id):
    cursor.execute("SELECT * FROM for_telebot WHERE ID=%s", [id])
    specific_data = cursor.fetchone()
    
    cursor.execute("DELETE FROM for_telebot WHERE id = %s", [id])
    connection.commit()
    return specific_data
