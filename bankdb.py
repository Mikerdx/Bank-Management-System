# bankdb.py
import sqlite3

DB_NAME = "bankdb.sqlite"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    con = get_connection()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS account (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            userName TEXT UNIQUE,
            userPW TEXT NOT NULL,
            balance INTEGER DEFAULT 0
        );
    """)
    con.commit()
    con.close()

def insert_user(userName, userPW):
    con = get_connection()
    cur = con.cursor()
    cur.execute("INSERT INTO account (userName, userPW) VALUES (?, ?)", (userName, userPW))
    con.commit()
    con.close()

def get_user_credentials(userName):
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT userPW, balance FROM account WHERE userName = ?", (userName,))
    data = cur.fetchone()
    con.close()
    return data

def update_balance(userName, new_balance):
    con = get_connection()
    cur = con.cursor()
    cur.execute("UPDATE account SET balance = ? WHERE userName = ?", (new_balance, userName))
    con.commit()
    con.close()

def get_balance(userName):
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT balance FROM account WHERE userName = ?", (userName,))
    data = cur.fetchone()
    con.close()
    return data[0] if data else None
