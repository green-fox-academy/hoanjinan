SELECT * FROM users
	JOIN reviews
	ON users.id = reviews.user_id;

CREATE VIEW users_for_marketing AS SELECT CONCAT(first_name, ' ', last_name), country FROM users;

SELECT * FROM users_for_marketing

DROP VIEW users_for_marketing

CREATE VIEW users_for_marketing AS SELECT CONCAT(first_name, ' ', last_name) AS full_name, country FROM users;

CREATE VIEW users_for_marketing AS SELECT CONCAT(first_name, ' ', last_name) AS full_name, country FROM users
	WHERE first_name IS NOT NULL AND last_name IS NOT NULL and country IS NOT NULL;

SELECT * FROM users_for_marketing LIMIT 10;

--bad
SELECT AVG(price) FROM products;
SELECT * FROM products
	WHERE price > 79.32;

--good
SELECT * FROM products
	WHERE price > (SELECT AVG(price) FROM products);

CREATE VIEW around_average AS SELECT * FROM products
	WHERE price BETWEEN (SELECT AVG(price) FROM products) - 10
	AND (SELECT AVG(price) FROM products) + 10 LIMIT 10;

SELECT * FROM around_average



