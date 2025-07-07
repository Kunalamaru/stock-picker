import sqlite3
from datetime import datetime, timedelta

DB = "history.db"

def get_current_thresholds():
    # Default thresholds (can evolve)
    return {
        "rsi_buy": 40,
        "sentiment_buy": 0.3,
        "profit_target": 1.035
    }

def record_trade(symbol, entry, target_exit, sentiment, rsi, action):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS trades (
            symbol TEXT, entry REAL, exit_target REAL, sentiment REAL,
            rsi REAL, action TEXT, date TEXT, actual_exit REAL DEFAULT NULL
        )
    ''')
    c.execute('''
        INSERT INTO trades (symbol, entry, exit_target, sentiment, rsi, action, date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (symbol, entry, target_exit, sentiment, rsi, action, datetime.now().date()))
    conn.commit()
    conn.close()

# In future, a daily script could fetch actual close prices & backfill `actual_exit` to improve accuracy.
