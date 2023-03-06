/* Задача 1
Создайте таблицу с мобильными телефонами,
 используя графический интерфейс.
 Заполните БД данными (поля и наполнение см. в презентации)
*/
CREATE TABLE Phone (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, 
	product_name VARCHAR(45) NOT NULL, 
	manufacturer VARCHAR(45) NOT NULL,
    product_count INT,
    price INT
);
INSERT INTO Phone (prodact_name, manufacturer, product_count, price)
VALUES 
('iPhone X', 'Apple', '3', '76000'),
('iPhone 8', 'Apple', '2', '51000'),
('Galaxy S9', 'Samsung', '2', '56000'),
('Galaxy S8', 'Samsung', '1', '41000'),
('P20 Pro', 'Huawei', '5', '36000');
/* . Выведите название, производителя и цену для товаров, количество
которых превышает 2
*/
SELECT prodact_name, manufacturer, price FROM Phone
WHERE product_count > 2;

/*Выведите весь ассортимент товаров марки “Samsung”
*/
SELECT * FROM 	Phone WHERE manufacturer = "Samsung" 