-- lists all records of the table second_table of the database
SELECT score, name
FROM second_table
WHERE names IS NOT NULL
ORDER BY score DESC;