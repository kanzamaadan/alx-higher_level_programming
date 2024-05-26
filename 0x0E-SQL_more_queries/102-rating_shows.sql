-- lists all genres from hbtn_0d_tvshows
SELECT tv_shows.title, SUM(rate) AS rating
FROM tv_shows
INNER JOIN tv_show_ratings
ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating DESC;
