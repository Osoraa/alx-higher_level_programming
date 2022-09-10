-- Lists all the cities in a specific state
SELECT c.id, c.name
FROM states AS s
    JOIN cities AS c
WHERE s.name = "California";
