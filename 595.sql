# Runtime: 1757 ms, faster than 52.79% of MySQL online submissions for Big Countries.
# Difficulty: Easy

SELECT name, population, area
FROM World
WHERE area > 3000000 OR population > 25000000
