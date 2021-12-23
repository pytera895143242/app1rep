import sqlite3

db = sqlite3.connect('lang.db')
sql = db.cursor()

def reg_bd():
    sql.execute(""" CREATE TABLE IF NOT EXISTS users (
            chat_id,
            lang
            ) """)
    db.commit()

def reg_lang(chat_id,lang):
    sql.execute(f"SELECT chat_id FROM users WHERE chat_id ='{chat_id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?,?)", (str(chat_id),lang))
        db.commit()
    else:
        try:
            sql.execute(f"UPDATE users SET lang = '{lang}' WHERE chat_id ='{chat_id}'")
            db.commit()
        except:
            pass


def cheack_lang(chat_id):
    lang = (sql.execute(f"SELECT lang FROM users WHERE chat_id = '{chat_id}'").fetchall())[0][0]
    return lang