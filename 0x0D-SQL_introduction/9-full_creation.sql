-- create a table using CREATE
-- DDL query to create a table if dose not exists
CREATE TABLE IF NOT EXISTS second_table
(id INT,
name VARCHAR(256),
score INT)
-- DML query to insert first row in table
INSERT INTO second_table(id,name,score)
VALUES (1'John',10);
-- DML query to insert second row in table
INSERT INTO second_table(id,name,score)
VALUES (2,'Alex',3);
-- DML query to insert third row in table
INSERT INTO second_table(id,name,score)
VALUES (3,'Bob',14);
-- DML query to insert fouth row in table
INSERT INTO second_table(id,name,score)
VALUES (4,'George',8);
