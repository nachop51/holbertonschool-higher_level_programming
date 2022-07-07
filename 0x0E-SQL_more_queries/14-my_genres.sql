-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT s.name FROM tv_genres s JOIN tv_show_genres t ON s.id = t.genre_id JOIN tv_shows g ON g.id = t.show_id WHERE g.title = 'Dexter' ORDER BY s.name;
