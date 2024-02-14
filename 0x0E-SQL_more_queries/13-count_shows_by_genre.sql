-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT myGenres.`name` AS `genre`, COUNT(*) AS `number_of_shows`
FROM `tv_genres` AS myGenres INNER JOIN `tv_show_genres` AS t
ON myGenres.`id` = t.`genre_id` GROUP BY myGenres.`name`ORDER BY `number_of_shows` DESC;
