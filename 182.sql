# Runtime: 185 ms, faster than 67.53% of MySQL online submissions for Duplicate Emails.
# Difficulty: Easy

select Email from Person group by Email having count(*) > 1;
