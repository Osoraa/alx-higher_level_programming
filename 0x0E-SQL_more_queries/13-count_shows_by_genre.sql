-- Lists all genres and number of shows linked shows
SELECT name, count(name) AS number_of_shows
FROM tv_genres JOIN tv_show_genres ON id = genre_id
GROUP BY name
ORDER BY number_of_shows desc;
