DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    full_name VARCHAR(100),
    age INT,
    position VARCHAR(50),
    phone VARCHAR(20)
);

INSERT INTO employees (id, full_name, age, position, phone)
VALUES
(1, 'Dilshod Rahimov', 26, 'Dasturchi', '907654321'),
(2, 'Aziz Tursunov', 32, 'Menejer', '918765432'),
(3, 'Madina Yusupova', 27, 'Dizayner', NULL),
(4, 'Otabek Nazarov', 38, 'Direktor', '935432109'),
(5, 'Sherzod Qodirov', 24, 'Dasturchi', '946543210');

SELECT * FROM employees;

DROP TABLE employees;