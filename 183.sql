# Runtime: 237 ms, faster than 70.62% of MySQL online submissions for Customers Who Never Order.
# Difficulty: Easy

select Name as Customers from Customers
where Id not in (select CustomerId from Orders)
