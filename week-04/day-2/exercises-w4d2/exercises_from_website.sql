-- How can you produce a list of the start times for bookings by members named 'David Farrell'?
SELECT starttime FROM cd.bookings
	JOIN cd.members
	ON cd.bookings.memid = cd.members.memid
	WHERE firstname = 'David' AND surname = 'Farrell';

-- How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'?
-- Return a list of start time and facility name pairings, ordered by the time.
SELECT starttime AS start, name FROM cd.bookings
	JOIN cd.facilities
	ON cd.bookings.facid = cd.facilities.facid
	WHERE name LIKE 'Tennis Court%'
	AND starttime::date = '2012-09-21'
	ORDER BY start;
	
-- How can you output a list of all members who have recommended another member?
-- Ensure that there are no duplicates in the list, and that results are ordered by (surname, firstname).
SELECT DISTINCT membs.firstname, membs.surname FROM cd.members membs
	JOIN cd.members membs_itself
	ON membs.memid = membs_itself.recommendedby
	ORDER BY surname, firstname;

-- How can you output a list of all members, including the individual who recommended them (if any)?
-- Ensure that results are ordered by (surname, firstname).
SELECT membs.firstname, membs.surname, membs_itself.firstname, membs_itself.surname FROM cd.members membs
	LEFT OUTER JOIN cd.members membs_itself
	ON membs_itself.memid = membs.recommendedby
	ORDER BY membs.surname, membs.firstname;

-- How can you produce a list of all members who have used a tennis court?
-- Include in your output the name of the court, and the name of the member formatted as a single column.
-- Ensure no duplicate data, and order by the member name.
SELECT DISTINCT CONCAT(firstname, ' ', surname) AS member, name FROM cd.members
	JOIN cd.bookings
	ON cd.members.memid = cd.bookings.memid
	JOIN cd.facilities
	ON cd.bookings.facid = cd.facilities.facid
	WHERE name LIKE 'Tennis Court%'
	ORDER BY member;
	
-- How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30?
-- Remember that guests have different costs to members (the listed costs are per half-hour 'slot'),
-- and the guest user is always ID 0. Include in your output the name of the facility,
-- the name of the member formatted as a single column, and the cost.
-- Order by descending cost, and do not use any subqueries.



-- How can you output a list of all members, including the individual who recommended them (if any), without using any joins?
-- Ensure that there are no duplicates in the list, and that each firstname + surname pairing is formatted as a column and ordered.



-- How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30?
-- Remember that guests have different costs to members (the listed costs are per half-hour 'slot'),
-- and the guest user is always ID 0. Include in your output the name of the facility,
-- the name of the member formatted as a single column, and the cost.
-- Order by descending cost.






















































