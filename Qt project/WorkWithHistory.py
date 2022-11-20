import sqlite3


# получение истоиии запросов к сайту yahoo fin
def get_history():
    con = sqlite3.connect("History.sqlite")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM History""").fetchall()

    li = list()
    for elem in result:
        li.append(elem)
    con.close()
    return li


# добовление элемента в бд
def add_item_to_history(name, weight, divider, date_from, date_to):
    con = sqlite3.connect("History.sqlite")
    cur = con.cursor()

    cur.execute(f"""INSERT INTO History()
     VALUES({name}, {weight}, {divider}, {date_from}, {date_to})""").fetchall()
    con.close()


# удаление всех элементов из бд
def clear_history():
    con = sqlite3.connect("History.sqlite")
    cur = con.cursor()

    cur.execute("""DELETE FROM History""").fetchall()
    con.close()
