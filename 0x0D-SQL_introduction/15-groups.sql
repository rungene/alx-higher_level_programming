-- Display same score using COUNT, ORDER BY, GROUP BY
-- DML query to display the number of records with the same score
SELECT score, COUNT(*) AS 'number'
FROM second_table
GROUP BY score
ORDER BY score DESC;
