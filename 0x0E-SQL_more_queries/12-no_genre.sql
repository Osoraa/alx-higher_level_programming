-- Lists all shows contained in a database without a linked genre
SELECT title, genre_id
FROM tv_shows LEFT JOIN tv_show_genres ON id = show_id
WHERE show_id IS NULL;
ORDER BY title, genre_id;
