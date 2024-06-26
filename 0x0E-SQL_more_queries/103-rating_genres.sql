-- lists all genres from hbtn_0d_tvshows
SELECT tv_genres.name, SUM(rate) AS rating
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_show_ratings
ON tv_show_ratings.show_id = tv_show_genres.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
