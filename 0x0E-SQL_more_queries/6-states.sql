-- create a database and table if not exists
-- DDL query
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create a table in MYSQL server states
CREATE TABLE IF NOT EXISTS states (
id INT NOT NULL AUTO_INCREMENT UNIQUE,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id)
);
Create database and table
