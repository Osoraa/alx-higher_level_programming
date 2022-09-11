-- Lists all shows of the Comedy genre
SELECT title
FROM tv_shows AS tvs
JOIN tv_show_genres ON tvs.id = show_id
JOIN tv_genres AS tvg ON genre_id = tvg.id
WHERE tvg.name = "Comedy"
ORDER BY title;
