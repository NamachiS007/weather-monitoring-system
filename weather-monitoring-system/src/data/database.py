import sqlite3

class Database:
    def __init__(self, db_name='weather.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS daily_summaries (
                date TEXT PRIMARY KEY,
                average_temp REAL,
                max_temp REAL,
                min_temp REAL,
                dominant_condition TEXT
            )
        ''')
        self.connection.commit()

    def insert_daily_summary(self, date, average_temp, max_temp, min_temp, dominant_condition):
        self.cursor.execute('''
            INSERT OR REPLACE INTO daily_summaries (date, average_temp, max_temp, min_temp, dominant_condition)
            VALUES (?, ?, ?, ?, ?)
        ''', (date, average_temp, max_temp, min_temp, dominant_condition))
        self.connection.commit()

    def close(self):
        self.connection.close()