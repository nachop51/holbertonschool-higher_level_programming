-- script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT s.title FROM tv_shows s JOIN tv_show_genres t ON s.id = t.show_id JOIN tv_genres g ON g.id = t.genre_id WHERE g.name = 'Comedy' ORDER BY s.title;
