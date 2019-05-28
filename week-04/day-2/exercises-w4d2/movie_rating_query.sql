--Find the titles of all movies directed by Steven Spielberg. 
SELECT title, director FROM movie
	WHERE director = 'Steven Spielberg';

--Find all years that have a movie that received a rating of 4 or 5, and sort them in increasing order. 
SELECT DISTINCT title FROM movie
	JOIN rating
	ON movie.mid = rating.mid
	WHERE stars = 4 OR stars = 5;

--Find the titles of all movies that have no ratings. 
SELECT title FROM movie
	LEFT JOIN rating
	ON movie.mid = rating.mid
	WHERE stars IS NULL;

--Some reviewers didn't provide a date with their rating. Find the names of all reviewers who have ratings with a NULL value for the date. 
SELECT name FROM reviewer
	JOIN rating
	ON reviewer.rid = rating.rid
	WHERE ratingdate IS NULL;

--Write a query to return the ratings data in a more readable format: reviewer name, movie title, stars, and ratingDate. Also, sort the data, first by reviewer name, then by movie title, and lastly by number of stars. 
SELECT name, title, stars, ratingdate FROM rating
	JOIN reviewer
	ON rating.rid = reviewer.rid
	JOIN movie
	ON rating.mid = movie.mid
	ORDER BY name, title, stars;

--EXTRA EXERCISES
--Find the names of all reviewers who rated Gone with the Wind.
SELECT DISTINCT name FROM reviewer
	JOIN rating
	ON reviewer.rid = rating.rid
	JOIN movie
	ON rating.mid = movie.mid
	WHERE title = 'Gone with the Wind';

--For any rating where the reviewer is the same as the director of the movie, return the reviewer name, movie title, and number of stars.
SELECT name, title, stars FROM reviewer
	JOIN rating
	ON reviewer.rid = rating.rid
	JOIN movie
	ON rating.mid = movie.mid
	WHERE director = name;






