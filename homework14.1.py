import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f"User{i}", f"example{i}@gmail.com", f"{i}0", "1000"))

# for i in range(1, 11, 2):
#     cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, f"{i}"))

# for i in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users WHERE id = ?", (f"{i}",))

# cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))  # Удаляем id под номером 6
cursor.execute("SELECT COUNT(*) FROM Users")  # Считаем количество пользователей в БД
all_users = cursor.fetchone()[0]
print(all_users)
cursor.execute("SELECT SUM(balance) FROM Users")  # Считаем общую сумму на балансе всех пользователей в БД
all_balance = cursor.fetchone()[0]
print(all_balance)
cursor.execute("SELECT AVG(balance) FROM Users")  # Считаем среднюю сумму по всем пользователям.
avg_balance = cursor.fetchone()[0]
print(avg_balance)

connection.commit()
connection.close()
