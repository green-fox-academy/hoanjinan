CREATE TABLE todo(
	todo_id BIGSERIAL NOT NULL PRIMARY KEY,
	task VARCHAR(100));
	
INSERT INTO todo (task) VALUES('Walk the dog');
INSERT INTO todo (task) VALUES('Buy milk');
INSERT INTO todo (task) VALUES('Do homework');