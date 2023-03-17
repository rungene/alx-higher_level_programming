-- create a database if not exists
-- DDL query
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create a table in MYSQL server states
-- DDL query to create a table and with attributes: id and name. id INT unique, auto generated, can’t be null and is a primary key
CREATE TABLE IF NOT EXISTS states (
id INT NOT NULL AUTO_INCREMENT UNIQUE,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id)
);
