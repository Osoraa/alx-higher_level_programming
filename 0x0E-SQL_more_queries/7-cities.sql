-- Creates a database
-- Creates a table with id and name columns in the new database
-- id should be pk and should auto-increment
-- name should non-null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    state_id INT NOT NULL,
        FOREIGN KEY(state_id) REFERENCES states(id),
    name VARCHAR(256) NOT NULL
);
