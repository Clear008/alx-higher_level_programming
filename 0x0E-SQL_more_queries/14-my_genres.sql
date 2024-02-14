-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
SELECT myGenres.`name` FROM `tv_genres` AS myGenres INNER JOIN `tv_show_genres` AS myShows
ON myGenres.`id` = myShows.`genre_id` INNER JOIN `tv_shows` AS t
ON t.`id` = myShows.`show_id` WHERE t.`title` = "Dexter" ORDER BY myGenres.`name`;
