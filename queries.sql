-- получить все книги
SELECT * FROM books;

-- получить первые 3 книги
SELECT * FROM books LIMIT 3;

-- получить книги отсортировав по названию

-- получить книги отсортировав в обратном порядке

-- получить книгу по id
SELECT * FROM books WHERE id = 1;

-- получить книгу по названию
SELECT * FROM books WHERE name = 'Гарри Поттер';

-- получить книгу по цене
SELECT * FROM books WHERE duration BETWEEN 500 AND 3000;

-- Добавить таблица с авторами
CREATE TABLE author (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    book_id INTEGER,
    FOREIGN KEY (book_id) REFERENCES books(id)
);

-- Внести данные в таблицу авторов
INSERT INTO authors (name, book_id) VALUES
    ('Льюис Кэрролл', 1),
    ('Антон Чехов', 2),
    ('Джоан Роулинг', 3)

-- получить всех авторов одной книги
SELECT * FROM books WHERE book_id = 1;

-- получить авторов с названием книги
SELECT t.name, c.name FROM authors AS
JOIN books AS c ON t.book_id = c.id

-- получить преподавателей с названием курса, фильтр по id курса
SELECT t.name, c.name FROM books AS t
JOIN author AS c ON t.book_id = c.id
WHERE c.id = 1;

--сохранение результата опросник


