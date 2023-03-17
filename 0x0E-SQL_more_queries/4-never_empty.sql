-- create a table in MYSQL server id_not_null
-- DDL query to create a table and with attributes: id and name
CREATE TABLE IF NOT EXISTS id_not_null (
id INT DEFAULT 1,
name VARCHAR(256) NOT NULL
);
