import queue
import sqlite3

with sqlite3.connect('caldb\database.db') as db:
    cursor = db.cursor()
    # query =  """CREATE TABLE IF NOT EXISTS clients(id INTEGER, kod TEXT, name TEXT) """  #Создание таблицы
    query = """ INSERT INTO clients(id, kod, name) VALUES(2, "FI-793", "ООО Симахов") """ #Добавление данных
    query1 = """ INSERT INTO clients(id, kod, name) VALUES(3, "FA-694", "ИП Усачева") """ #Добавление данных
    cursor.execute(query)
    cursor.execute(query1)
    db.commit() #Рекомендуется перед закрытием соединения с БД
