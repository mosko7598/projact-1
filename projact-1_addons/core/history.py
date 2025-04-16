import sqlite3
from datetime import date

def save_value(value):
    conn = sqlite3.connect("data/value_history.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS history (date TEXT PRIMARY KEY, value REAL)")
    cursor.execute("INSERT OR REPLACE INTO history (date, value) VALUES (?, ?)", (str(date.today()), value))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect("data/value_history.db")
    cursor = conn.cursor()
    cursor.execute("SELECT date, value FROM history ORDER BY date ASC")
    rows = cursor.fetchall()
    conn.close()
    return [{"date": r[0], "value": r[1]} for r in rows]
