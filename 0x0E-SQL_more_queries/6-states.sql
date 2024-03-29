-- Creates a database
-- Creates a table with id and name columns in the new database
-- id should be pk and should auto-increment
-- name should non-null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);
