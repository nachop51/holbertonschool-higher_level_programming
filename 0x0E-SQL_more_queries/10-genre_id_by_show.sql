-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT s.title, g.genre_id FROM tv_shows s INNER JOIN tv_show_genres g ON s.id = g.show_id ORDER BY s.title, g.genre_id;