-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT s.title, g.name FROM tv_shows s LEFT JOIN tv_show_genres t ON s.id = t.show_id LEFT JOIN tv_genres g ON g.id = t.genre_id ORDER BY s.title, g.name;
