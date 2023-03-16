-- lists sorted records of the table using ORDER BY
-- DML query to display sorted table sorted by score >= 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
