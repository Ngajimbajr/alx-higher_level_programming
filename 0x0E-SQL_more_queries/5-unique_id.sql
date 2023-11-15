-- Specify the database name as an argument when executing the script

-- Create table unique_id if not exists
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

-- If you want to set id as a primary key, uncomment the following line
-- ALTER TABLE unique_id ADD PRIMARY KEY (id);
