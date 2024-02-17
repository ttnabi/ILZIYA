import sqlite3
from pathlib import Path
from pprint import pprint


class DB:
    def __init__(self):
        """Инициализация соединения с БД"""
        # .db, .db3, .sqlite, .sqlite3
        self.connection = sqlite3.connect(Path(__file__).parent.parent / 'db.sqlite3')
        self.cursor = self.connection.cursor()

    def create_tables(self):
        """Создание таблиц"""
        self.cursor.execute('DROP TABLE IF EXISTS books')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books ( 
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT, 
                description TEXT, 
                duration INTEGER, 
                image TEXT 
            ) 
        ''')

    def populate_tables(self):
        """Заполнение таблиц"""
        self.cursor.execute('''
            INSERT INTO books (name, description, duration, image) VALUES  
            ("Властелин колец", "Властелин колец-это...",3,"images/Lord of the Rings.jpg"), 
            ("Гарри Поттер", "Гарри Поттер-это...", 7,"images/Harry Potter.jpg"), 
            ("Вишневый сад", "Вишневый сад- это...",4,"images/The Cherry Orchard.jpg"), 
            ("Мистер X", "Мистер X-это...",2, "images/Mister X.jpg"), 
            ("Алиса в стране чудес", "Алиса в стране чудес-это ...",2, "images/Alice in Wonderland.jpg") 
        ''')
        self.connection.commit()

    def get_books(self):
        """Получение книг"""
        self.cursor.execute('SELECT * FROM books')
        return self.cursor.fetchall()


if __name__ == "__main__":
    db = DB()
    db.create_tables()
    db.populate_tables()
    pprint(db.get_books())

# СУБД - Система Управления Базами Данных
# MySQL, PostgreSQL, SQLite, Oracle, MsSQL
# PRIMARY KEY - первичный ключ
