-- Lists all rows with a name value
SELECT score, name
FROM second_table
WHERE name is NOT NULL
ORDER BY score DESC;
