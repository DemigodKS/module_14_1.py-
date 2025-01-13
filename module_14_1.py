import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

#обращаемся к базе данных
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
i=1
age_= 0
#ЗАПОЛНЯЕМ 10-Ю ЗАПИСЯМИ
#for i in range(1, 11):
    #age_ += 10
    #cursor.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                  #(f"User{i}", f"example{i}@gmail.com", f"{age_}", "1000"))
#обновить баланс
#cursor.execute(" UPDATE Users SET balance = 500 WHERE id % 2 != 0")

#delete
#cursor.execute(" DELETE FROM Users WHERE id IN (1, 4, 7, 10)")

#cursor.execute(" DROP TABLE Users")

cursor.execute(" SELECT username, email, age, balance FROM Users WHERE age != 60")
#возвращаем список кортежей
users = cursor.fetchall()

for user_ in users:
   print("Имя:",user_[0],"|", "Почта:",user_[1], "|","Возраст",user_[2],"|","Баланс:",user_[3])
connection.commit()
connection.close()