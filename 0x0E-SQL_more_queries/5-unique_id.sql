-- create a table in MYSQL server unique_id
-- DDL query to create a table and with attributes: id and name. id default value = 1, must be unique
CREATE TABLE IF NOT EXISTS unique_id (
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256) NOT NULL
);
