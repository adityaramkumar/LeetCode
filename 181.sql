# Runtime: 293 ms, faster than 71.46% of MySQL online submissions for Employees Earning More Than Their Managers.
# Difficulty: Easy

select employee.Name as Employee
from Employee as employee, Employee as manager
where employee.ManagerId = manager.Id and employee.Salary > manager.Salary;
