CREATE TABLE users(
	user_id VARCHAR(20) NOT NULL PRIMARY KEY
);

CREATE TABLE messages(
	message_id TEXT NOT NULL PRIMARY KEY,
	user_id	VARCHAR(20) REFERENCES users(user_id),
	message TEXT,
	channel VARCHAR(20)
);

CREATE TABLE reactions(
	reaction_id BIGSERIAL NOT NULL PRIMARY KEY,
	user_id	VARCHAR(20) REFERENCES users(user_id),
	message_id TEXT REFERENCES messages(message_id),
	reaction VARCHAR(50) NOT NULL
);

CREATE TABLE mentions(
	message_id TEXT REFERENCES messages(message_id),
	user_id	VARCHAR(20) REFERENCES users(user_id)
);