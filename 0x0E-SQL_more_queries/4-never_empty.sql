-- Specify the database name as an argument when executing the script

-- Create table id_not_null if not exists
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

-- If you want to set id as a primary key, uncomment the following line
-- ALTER TABLE id_not_null ADD PRIMARY KEY (id);
