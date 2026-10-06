DROP TABLE IF EXISTS cars;

CREATE TABLE cars (
    id INT PRIMARY KEY,
    brand VARCHAR(50),
    model VARCHAR(50),
    year INT,
    color VARCHAR(30),
    owner VARCHAR(100)
);

INSERT INTO cars (id, brand, model, year, color, owner)
VALUES
(1, 'Chevrolet', 'Gentra', 2021, 'Oq', 'Dilshod Rahimov'),
(2, 'Chevrolet', 'Tracker', 2023, 'Kulrang', NULL),
(3, 'Kia', 'Sportage', 2022, 'Qora', 'Madina Yusupova'),
(4, 'Toyota', 'Land Cruiser', 2024, 'Ko''k', NULL),
(5, 'Hyundai', 'Tucson', 2023, 'Oq', 'Otabek Nazarov'),
(6, 'BYD', 'Han', 2024, 'Qizil', 'Sherzod Qodirov'),
(7, 'Nissan', 'Qashqai', 2021, 'Kulrang', NULL);

SELECT * FROM cars;

DROP TABLE cars;

CREATE TABLE cars (
    id INT PRIMARY KEY,
    brand VARCHAR(50),
    model VARCHAR(50),
    year INT,
    color VARCHAR(30),
    owner VARCHAR(100)
);

INSERT INTO cars (id, brand, model, year, color, owner)
VALUES
(1, 'Chevrolet', 'Spark', 2023, 'Oq', 'Dilshod'),
(2, 'Kia', 'Rio', 2022, 'Qora', 'Aziz'),
(3, 'Toyota', 'RAV4', 2024, 'Ko''k', 'Madina');

SELECT * FROM cars;