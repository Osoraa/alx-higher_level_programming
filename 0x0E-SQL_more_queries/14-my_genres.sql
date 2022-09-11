-- Lists all genres of a the Dexter show
SELECT name
FROM tv_genres AS tvg
JOIN tv_show_genres ON tvg.id = genre_id
JOIN tv_shows AS tvs ON show_id = tvs.id
WHERE tvs.title = "Dexter"
ORDER BY name ASC;
