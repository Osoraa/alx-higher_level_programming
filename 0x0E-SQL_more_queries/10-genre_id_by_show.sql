-- Liss all shows contained in a database with a linked genre
SELECT title, genre_id
FROM tv_shows JOIN tv_show_genres ON id = show_id
ORDER BY title, genre_id;
