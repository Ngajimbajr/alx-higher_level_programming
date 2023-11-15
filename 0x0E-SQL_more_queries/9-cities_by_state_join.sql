-- Specify the database name as an argument when executing the script

-- Switch to the hbtn_0d_usa database
USE hbtn_0d_usa;

-- List all cities with their IDs, names, and corresponding state names
SELECT cities.id, cities.name, states.name AS state_name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
