-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT s.name AS genre, COUNT(t.genre_id) AS number_of_shows FROM tv_genres s RIGHT JOIN tv_show_genres t ON s.id = t.genre_id GROUP BY s.name ORDER BY number_of_shows DESC;
