# Runtime: 330 ms, faster than 35.42% of MySQL online submissions for Swap Salary.
# Difficulty: Easy

UPDATE SALARY
SET sex = IF(sex = 'f', 'm', 'f'); 
