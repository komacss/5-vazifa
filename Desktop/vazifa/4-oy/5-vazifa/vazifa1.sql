DROP TABLE IF EXISTS books;

CREATE TABLE books (
    id INT PRIMARY KEY,
    title VARCHAR(50),
    author VARCHAR(50),
    year INT,
    description VARCHAR(150)
);

INSERT INTO books (id, title, author, year, description)
VALUES
(1, 'Atom odatlar', 'Jeyms Klir', 2018, 'Yaxshi odatlarni shakllantirish haqida kitob'),
(2, 'Otkan kunlar', 'Abdulla Qodiriy', 1925, 'Ozbek adabiyotining mashhur romani'),
(3, 'Alkimyogar', 'Paulo Koelyo', 1988, NULL),
(4, 'Ikki eshik orasi', 'Otkir Hoshimov', 1987, NULL),
(5, 'Sariq devni minib', 'Xudoyberdi Toxtaboyev', 1968, 'Qiziqarli bolalar sarguzasht asari');

SELECT * FROM books;