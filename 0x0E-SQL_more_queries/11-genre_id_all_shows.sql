-- Liss all shows contained in a database with a linked genre
-- Show NULL on no linked genre
-- Synonym: Genre ID for all shows
SELECT title, genre_id
FROM tv_shows LEFT JOIN tv_show_genres ON id = show_id
order by title, genre_id;
