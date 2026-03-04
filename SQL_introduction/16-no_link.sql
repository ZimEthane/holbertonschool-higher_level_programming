-- List records with a non-null name, ordered by score descending
SELECT score, name  FROM second_table where name IS NOT NULL and name != '' ORDER BY score DESC;
