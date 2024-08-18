import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

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


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    return products


connection.commit()
