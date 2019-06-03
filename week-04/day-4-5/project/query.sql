-- Who sent the most messages to the thanks channel?
SELECT user_id AS users, COUNT(user_id) AS user_count FROM messages
	WHERE channel = 'Thanks'
	GROUP BY users
	ORDER BY user_count DESC;

-- Which emoji is the most common as reaction in the thanks channel?
SELECT reaction, COUNT(reaction) AS emoji_count FROM reactions
	JOIN messages
	ON reactions.message_id = messages.message_id
	WHERE channel = 'Thanks'
	GROUP BY reaction
	ORDER BY emoji_count DESC;

-- Who reacted to the most messages?
SELECT user_id AS users, COUNT(user_id) AS reaction_count FROM reactions
	GROUP BY users
	ORDER BY reaction_count DESC;

-- Who is the most mentioned person in the thanks channel?
SELECT mentions.user_id AS users, COUNT(mentions.user_id) AS mention_count FROM mentions
	JOIN messages
	ON mentions.message_id = messages.message_id
	WHERE channel = 'Thanks'
	GROUP BY users
	ORDER BY mention_count DESC;

-- Which message got the most reactions in the thanks channel?
SELECT reactions.message_id, COUNT(reactions.message_id) AS reaction_count FROM reactions
	JOIN messages
	ON reactions.message_id = messages.message_id
	WHERE channel = 'Thanks'
	GROUP BY reactions.message_id
	ORDER BY reaction_count DESC;
