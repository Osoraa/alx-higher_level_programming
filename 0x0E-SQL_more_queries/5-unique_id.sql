-- Creates a table unique_id
-- Adds two columns id and name
-- id is type int with a unique default value 1 and name is varchar(256)
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
