DROP TABLE IF EXISTS products;

CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    price INT,
    category VARCHAR(50),
    description VARCHAR(150)
);

INSERT INTO products (id, name, price, category, description)
VALUES
(1, 'Non', 4000, 'Oziq-ovqat', 'Yangi yopilgan non'),
(2, 'Sut', 12000, 'Ichimlik', '1 litr sigir suti'),
(3, 'Telefon', 2500000, 'Elektronika', 'Smartfon'),
(4, 'Qalam', 3000, 'Kanselyariya', NULL),
(5, 'Daftar', 8000, 'Kanselyariya', '96 varoqli daftar'),
(6, 'Quloqchin', 150000, 'Elektronika', NULL);

SELECT * FROM products;

DROP TABLE products;