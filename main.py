import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Создание таблицы классов
cursor.execute('''CREATE TABLE IF NOT EXISTS classes
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   link TEXT,
                   lfyyst TEXT)''')

# Вставка данных в таблицу
cursor.execute("INSERT INTO classes (name, link, lfyyst) VALUES (?, ?, ?)", ('gismeteo', 'https://www.gismeteo.by/', 'данные1'))
cursor.execute("INSERT INTO classes (name, link, lfyyst) VALUES (?, ?, ?)", ('Класс 2', 'ссылка2', 'данные2'))
cursor.execute("INSERT INTO classes (name, link, lfyyst) VALUES (?, ?, ?)", ('Класс 3', 'ссылка3', 'данные3'))

# Получение данных из таблицы
cursor.execute("SELECT * FROM classes")
rows = cursor.fetchall()

# Вывод данных в виде таблицы
print("ID\tНазвание\tСсылка\t\tДанные")
for row in rows:
    print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t{row[3]}")

# Закрытие подключения к базе данных
conn.close() 