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
        self.cursor.execute('DROP TABLE IF EXISTS houses')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS houses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT, 
            price INTEGER,
            som_price INTEGER,
            house_description TEXT,
            address TEXT
            )
        ''')
        self.connection.commit()

    def insert_houses(self, data: dict):
        print(data)
        self.cursor.execute('''
            INSERT INTO houses (title, price, som_price, house_description, address)
            VALUES (:title, :price, :som_price, :house_description, :address);
            ''',
                            {
                                'title': data['title'],
                                'price': data['price'],
                                'som_price': data['som_price'],
                                'house_description': data['house_description'],
                                'address': data['address']
                            }
                            )
        self.connection.commit()


house = {'address': 'Бишкекб Джал-23 м-н (Нижний Джал)',
         'house_description': 'Сдается хорошая двухкомнатная квартира в нижнем Джале. '
                              '6 этаж из 9, две лоджии.Новые пластиковые окна. '
                              'Имеется кондиционер. Квартира очень теплая. с...',
         'price': 461,
         'som_price': 40000,
         'title': '2-комн. кв., 48 м2, 6 этаж из 9'}

# def create_tables(self):
#     """Создание таблиц"""
#     self.cursor.execute("DROP TABLE IF EXISTS authors")
#     self.cursor.execute("DROP TABLE IF EXISTS books")
#     self.cursor.execute('''CREATE TABLE authors(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,


#         name TEXT NOT NULL
#         )
#         ''')
#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS books(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         description TEXT,
#         duration INTEGER,
#         image TEXT,
#         author_id INTEGER,
#         FOREIGN KEY (author_id) REFERENCES authors(id)
#                 )
#                 ''')
#
#     def populate_tables(self):
#         """Заполнение таблиц"""
#         self.cursor.execute('''INSERT INTO authors(name) VALUES ("Льюис Кэрролл")''')
#         self.cursor.execute('''INSERT INTO authors(name) VALUES ("Антон Чехов")''')
#         self.cursor.execute('''INSERT INTO authors(name) VALUES ("Джоан Роулинг")''')
#
# #         self.cursor.execute('''
#                   INSERT INTO books (name, description, duration, image, author_id) VALUES
#                   ("Алиса в зазеркалье", "Алиса в зазеркалье-это...",2800,"images/Alice.jpg",1),
#                   ("Гарри Поттер", "Гарри Поттер-это...", 3000,"images/Harry Potter.jpg",3),
#                   ("Вишневый сад", "Вишневый сад- это...",1500,"images/The Cherry Orchard.jpg",2),
#                   ("Переполох", "Переполох-это...",1000, "images/Perepoloh.jpg",2),
#                   ("Алиса в стране чудес", "Алиса в стране чудес-это ...",2500, "images/Alice in Wonderland.jpg",1)
#               ''')
#         self.connection.commit()
#
#     def get_books(self):
#         """Получение книг"""
#         # Пропустить первые две книги и показать следующие две книги.
#         self.cursor.execute('SELECT id, name FROM books')
#         # self.cursor.execute('SELECT * FROM books LIMIT 2')
#         return self.cursor.fetchall()
#
#     def get_book_by_id(self, book_id):
#         # book_id = "1; DROP DATABASE test;"
#         """Получение книги по ID"""
#         self.cursor.execute('SELECT id,name FROM books WHERE id = :id',
#                             {'id': book_id})
#         return self.cursor.fetchone()
#
#     def get_book_by_name(self, book_name):
#         """Получение книги по названиию"""
#         self.cursor.execute(
#             'SELECT * FROM books WHERE name = :name',
#             {'name': book_name}
#         )
#         return self.cursor.fetchone()
#
#     def get_authors_by_books_id(self):
#         """Получение авторов"""
#         self.cursor.execute(
#             "SELECT FROM authors WHERE book_id = 1"
#         )
#         return self.cursor.fetchall()
#
#     def get_authors(self):
#         self.cursor.execute(
#             'SELECT * FROM authors'
#         )
#         return self.cursor.fetchall()
#
#     def get_book_by_author(self, author_id):
#         self.cursor.execute(
#             'SELECT * FROM books WHERE author_id = :author_id', {'author_id': author_id}
#         )
#         return self.cursor.fetchall()

#   db.populate_tables()
#   pprint(db.get_books())
#   pprint(db.get_book_by_id(1))
#   pprint(db.get_book_by_name('Гарри Поттер'))
#
#
# # СУБД - Система Управления Базами Данных
# # MySQL, PostgreSQL, SQLite, Oracle, MsSQL
# # PRIMARY KEY - первичный ключ
#
# # Реляционные БД - realtional - связи
#
# # Авторы
# # id, name, book_id
# "Льюис Кэрролл"
# "Антон Чехов"
# "Джоан Роулинг"
#
# # Книги
# #  id, name, description, duration, image
# "Алиса в зазеркалье", "Алиса в зазеркалье -это...", 2800, "images/Alice.jpg", 1
# "Гарри Поттер", "Гарри Поттер-это...", 3000, "images/Harry Potter.jpg", 3
# "Вишневый сад", "Вишневый сад- это...", 1500, "images/The Cherry Orchard.jpg", 2
# "Переполох", "Переполох-это...", 500, "images/Perepoloh.jpg", 2
# "Алиса в стране чудес", "Алиса в стране чудес-это ...", 2500, "images/Alice in Wonderland.jpg", 1
#
# # FOREIGN KEY - Внешние ключи
