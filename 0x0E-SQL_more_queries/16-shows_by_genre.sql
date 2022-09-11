-- Lists all genres for all shows
SELECT title, name
FROM tv_shows AS tvs
LEFT JOIN tv_show_genres ON tvs.id = show_id
LEFT JOIN tv_genres AS tvg ON genre_id = tvg.id
ORDER BY title, name;
