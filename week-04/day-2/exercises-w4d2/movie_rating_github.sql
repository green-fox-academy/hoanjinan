-- Create a view where you display the reviewer's name and the amount of their review
CREATE VIEW review_amount AS
SELECT reviewer.rid AS reviewer_id, name, count(rating.rid) AS rating_count FROM reviewer
	JOIN rating
	ON reviewer.rid = rating.rid
	GROUP BY reviewer.rid, name
	ORDER BY reviewer.rid;

SELECT * FROM review_amount;

-- Create a view where you display the movies which have no review
CREATE VIEW no_review AS
SELECT title FROM movie
	LEFT JOIN rating
	ON movie.mid = rating.mid
	WHERE rating.mid IS NULL;
	
SELECT * FROM no_review;

-- Create a view where you display all the directors (do not include null values)
CREATE VIEW all_directors AS
SELECT DISTINCT director FROM movie
	WHERE director IS NOT NULL;
	
SELECT * FROM all_directors;

-- Create a view where you display the movie title and the average rating
CREATE VIEW avg_rating AS
SELECT title, ROUND(AVG(stars)) AS average_rating FROM movie
	JOIN rating
	ON movie.mid = rating.mid
	GROUP BY title;

SELECT * FROM avg_rating;






