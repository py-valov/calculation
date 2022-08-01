import sqlite3
import datetime

# with sqlite3.connect('caldb\database.db') as db:
#     cursor = db.cursor()
#     # query =  """CREATE TABLE IF NOT EXISTS clients(id INTEGER, kod TEXT, name TEXT) """  #Создание таблицы
#     query = """ INSERT INTO clients(id, kod, name) VALUES(2, "FI-793", "ООО Симахов") """ #Добавление данных
#     query1 = """ INSERT INTO clients(id, kod, name) VALUES(3, "FA-694", "ИП Усачева") """ #Добавление данных
#     cursor.execute(query)
#     cursor.execute(query1)
#     db.commit() #Рекомендуется перед закрытием соединения с БД




# Добавление в базу несколько значений

def get_timestamp(y, m, d):
    return datetime.datetime.timestamp(datetime.datetime(y, m, d))

def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()

insert_payments = [
    (1, 30000, get_timestamp(2022, 8, 15), 2),
    (2, 150000, get_timestamp(2022, 8, 17), 1),
    (3, 2678, get_timestamp(2022, 8, 17), 3),
    (4, 437896.15, get_timestamp(2022, 8, 21), 1)
    ]


# with sqlite3.connect('caldb\database.db') as db:
#     cursor = db.cursor()
#     query2 =  """ INSERT INTO payment(id, amount, payment_date, expense_id) 
#                         VALUES(?,?,?,?); """  #Создание таблицы



#     cursor.executemany(query2, insert_payments)
#     db.commit() #Рекомендуется перед закрытием соединения с БД





# Получение из базы данных

with sqlite3.connect('caldb\database.db') as db:
    cursor = db.cursor()
    query2 =  """ SELECT * FROM payment JOIN clients ON clients.id = payment.expense_id """  #Создание таблицы



    cursor.execute(query2)
    for res in cursor:
        print(get_date(res[2]), res[5], res[6], "сумма:" ,res[1])