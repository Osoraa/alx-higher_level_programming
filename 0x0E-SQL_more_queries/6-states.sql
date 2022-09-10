-- Creates a database
-- Creats a table in the new database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.state
(
    id INT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
