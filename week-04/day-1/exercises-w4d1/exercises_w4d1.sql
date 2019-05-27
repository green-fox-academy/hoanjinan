-- Read and import sql file
-- \i <filename>


-- List the users who registered in 2018 with a .com email address and living in China
SELECT * FROM users
WHERE email LIKE '%.com'
AND country = 'China'
AND EXTRACT(YEAR FROM date_of_registration) = 2018;

-- How many users are there?
SELECT COUNT(*) AS num_of_users FROM users;

-- How many users registered in 2019?
SELECT COUNT(*) AS num_of_users_in_2019 FROM users
WHERE EXTRACT(YEAR FROM date_of_registration) = 2019;

-- How many users registered in January?
SELECT COUNT(*) AS num_of_users_in_2019 FROM users
WHERE EXTRACT(MONTH FROM date_of_registration) = 01;

-- Which country has the most users?
SELECT country, COUNT(country) AS num_of_users FROM users
GROUP BY country
ORDER BY num_of_users DESC LIMIT 1;

-- What is the gender ratio?
-- SELECT username, gender FROM users
-- WHERE gender IS NOT NULL;

SELECT round((SELECT COUNT(gender) AS num_of_males FROM users
	WHERE gender = 'Male')
	::decimal/
	(SELECT COUNT(gender) AS num_of_females FROM users
	WHERE gender = 'Female'), 2);

-- ?????????????????????????????????????????????
-- How many users left at least one field blank?
SELECT COUNT(*) FROM users
	WHERE id IS NULL
	OR username IS NULL
	OR email IS NULL
	OR date_of_registration IS NULL
	OR first_name IS NULL
	OR last_name IS NULL
	OR country IS NULL
	OR gender IS NULL;

-- Which are the 3 most expensive products?
SELECT name, price FROM products ORDER BY price DESC LIMIT 3;

-- Which are the 4th and 5th cheapest products?
SELECT name, price FROM products ORDER BY price OFFSET 3 LIMIT 2;

-- What is the average price for an electric product?
SELECT AVG(price) AS average_electronics_price FROM products
	WHERE category = 'Electronics';

-- How much would it cost me to buy all the toys?
SELECT SUM(price) AS average_electronics_price FROM products
	WHERE category = 'Toys';

-- What is the average rating?
SELECT AVG(rating) AS average_rating FROM reviews;

-- Which product has the best average rating?
SELECT product_id, name, AVG(rating) AS average_rating FROM reviews
	JOIN products
	ON reviews.product_id = products.id
	GROUP BY product_id, name
	ORDER BY average_rating DESC LIMIT 1;

-- Which product has the worst rating?
SELECT product_id, name, MIN(rating) AS worst_rating FROM reviews
	JOIN products
	ON reviews.product_id = products.id
	GROUP BY product_id, name
	ORDER BY worst_rating LIMIT 1;

-- Which products have no review?
SELECT product_id, name FROM reviews
	JOIN products
	ON reviews.product_id = products.id
	WHERE comment IS NULL;

-- How many reviews are 3 or below without comment?
SELECT product_id, name, count(*) FROM reviews
	JOIN products
	ON reviews.product_id = products.id
	WHERE comment IS NULL
	GROUP BY product_id, name
	HAVING count(*) < 3;

-- Which user reviewed the most?
SELECT user_id, username, COUNT(user_id) AS num_of_reviews FROM reviews
	JOIN users
	ON reviews.user_id = users.id
	GROUP BY user_id, username
	ORDER BY num_of_reviews DESC LIMIT 1;

-- List the average rating for each product
SELECT product_id, name, ROUND(AVG(rating)) AS average_rating FROM reviews
	JOIN products
	ON reviews.product_id = products.id
	GROUP BY product_id, name;

-- ???????????????????????????????????????????
-- How many days passed since the last review?
SELECT (SELECT CURRENT_DATE) - (SELECT date from reviews ORDER BY date DESC LIMIT 1);






















