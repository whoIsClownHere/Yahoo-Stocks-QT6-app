import sqlite3


def get_history():
    con = sqlite3.connect("History.sqlite")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM History""").fetchall()

    li = list()
    for elem in result:
        li.append(elem)
    con.close()
    return li


def add_item_to_history(name, weight, divider, date_from, date_to):
    con = sqlite3.connect("History.sqlite")
    cur = con.cursor()

    cur.execute(f"""INSERT INTO History()
     VALUES({name}, {weight}, {divider}, {date_from}, {date_to})""").fetchall()
    con.close()


def clear_history():
    con = sqlite3.connect("History.sqlite")
    cur = con.cursor()

    cur.execute("""DELETE FROM History""").fetchall()
    con.close()
