# Write your MySQL query statement below
with my_cte as(
select    Department.name as Department, Employee.name as Employee,  Employee.Salary,
DENSE_RANK()OVER(PARTITION BY Department.id
order by Employee.Salary desc
) as rn
from Employee
left join Department
on Employee.departmentId = Department.id
)
SELECT Department, Employee, Salary
FROM my_cte
WHERE rn <= 3;