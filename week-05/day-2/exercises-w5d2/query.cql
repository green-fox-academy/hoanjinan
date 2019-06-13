SELECT id, country_code FROM weather_station
	WHERE id = '724940:23234';

SELECT wsid, temperature, year, month, day, hour FROM raw_weather_data
	WHERE year = 2008 AND month = 6 AND day = 1 AND wsid = '724940:23234';

#DOESN'T WORK!
SELECT wsid, temperature, year, month, day, hour FROM raw_weather_data
	WHERE year = 2008 AND month = 6 AND day = 1 AND wsid = '724940:23234' AND hour BETWEEN 9 AND 15;
	
SELECT wsid, temperature, year, month, day, hour FROM raw_weather_data
	WHERE year = 2008 AND month = 6 AND day = 1 AND wsid = '724940:23234' AND hour > 9 AND hour < 15;