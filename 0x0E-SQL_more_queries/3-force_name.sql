-- Specify the database name as an argument when executing the script

-- Create table force_name if not exists
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

-- If you want to set id as a primary key, uncomment the following line
-- ALTER TABLE force_name ADD PRIMARY KEY (id);
