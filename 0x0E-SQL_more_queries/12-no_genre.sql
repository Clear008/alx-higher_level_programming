-- Lists all shows in the database hbtn_0d_tvshows without a genre linked.
FROM `tv_shows` AS myShows LEFT JOIN `tv_show_genres` AS myGenres ON myShows.`id` = myGenres.`show_id`
WHERE myGenres.`genre_id` IS NULL
ORDER BY myShows.`title`, myGenres.`genre_id`;
