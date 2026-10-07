DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS shops;

CREATE TABLE shops (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(100)
);

CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    price INT,
    shop_id INT,
    FOREIGN KEY (shop_id) REFERENCES shops(id)
);

INSERT INTO shops (id, name, address)
VALUES
(1, 'Korzinka', 'Fergana'),
(2, 'Makro', 'Yunusobod'),
(3, 'Mediapark', 'Mirobod');

INSERT INTO products (id, name, price, shop_id)
VALUES
(1, 'Non', 4000, 1),
(2, 'Sut', 12000, 1),
(3, 'Yogurt', 9000, 1),
(4, 'Qalam', 3000, 2),
(5, 'Daftar', 8000, 2),
(6, 'Ruchka', 5000, 2),
(7, 'Telefon', 2500000, 3),
(8, 'Quloqchin', 150000, 3),
(9, 'Zaryadka', 60000, 3);

SELECT * FROM shops;
SELECT * FROM products;
SELECT * FROM products WHERE shop_id = 1;

UPDATE products SET price = 4500 WHERE id = 1;
UPDATE products SET shop_id = 1 WHERE id = 6;
UPDATE shops SET name = 'Korzinka Plus', address = 'Sergeli' WHERE id = 1;

SELECT * FROM shops;
SELECT * FROM products;