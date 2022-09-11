-- Lists all genres of a show
SELECT name
FROM tv_genres AS tvg
JOIN tv_show_genres ON tvg.id = genre_id
JOIN tv_shows AS tvs ON show_id = tvs.id
WHERE tvs.id = 8;
