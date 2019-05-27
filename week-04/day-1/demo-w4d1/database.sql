\l
CREATE DATABASE epam;
\c epam
\d
CREATE TABLE users(
	name VARCHAR(50));
\d
\d users
INSERT INTO users (name) VALUES ('Steven');
SELECT * FROM users
INSERT INTO users (name) VALUES ('Steven');
SELECT * FROM users
SELECT * FROM users WHERE country = 'Peru';
SELECT * FROM users WHERE country = 'P%';
SELECT * FROM users WHERE country = 'P__u';
SELECT COUNT(*) FROM users;
SELECT country, COUNT(*) FROM users GROUP BY country;
SELECT country FROM users ORDER BY data_ofregistration;