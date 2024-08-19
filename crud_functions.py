import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()


# def initiate_db():
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INT PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INT NOT NULL
);
''')

# cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                ("Витамин A", "Витамин А является основным источником ретиноидов, которые играют важную роль "
#                              "в процессе развития клеток кожи и костной ткани, и каротиноидов, отвечающих за "
#                              "здоровье сетчатки глаза.", "2300"))
# cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                ("Витамин B", "«B-2 Рибофлавин» 100 мг — биологически активная добавка от Now Foods, которая "
#                              "способна восполнить дефицит витамина, играющего важную роль в поддержании здоровья "
#                              "человека.", "800"))
# cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                ("Витамин D", "Витамин Д3 — это важное питательное вещество, которое играет ключевую роль "
#                              "в поддержании здоровья волос, костей и зубов, а также в укреплении иммунной системы.",
#                 "1000"))
# cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                ("Витамин A&D", "Витамин A - необходим для поддержания здоровой эпителиальной ткани, которая "
#                                "находится в глазах, коже, дыхательной системе, желудочных и мочевыводящих путях. "
#                                "Витамин D - способствует усвоению кальция и транспорта кальция в костях. Тем самым "
#                                "идет поддержка костной системы и здоровье зубов.", "600"))


cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INT PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INT NOT NULL,
balance INT NOT NULL
);
''')


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    return products


def add_user(username, email, age):
    cursor.execute('''INSERT INTO Users ('username', 'email', 'age', 'balance') VALUES (?, ?, ?, ?)
    ''', (username, email, age, '1000'))
    connection.commit()


def is_included(username):
    check_user = cursor.execute('SELECT * FROM Users WHERE username=?', (username,)).fetchone()
    if check_user is None:
        check_user = False
    else:
        check_user = True
    return check_user


connection.commit()
