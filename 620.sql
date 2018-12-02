# Runtime: 139 ms, faster than 60.43% of MySQL online submissions for Not Boring Movies.
# Difficulty: Easy

SELECT * FROM cinema
WHERE id % 2 = 1 AND description <> 'boring'
ORDER BY -rating;
