# Write your MySQL query statement below

select tbl.dname as Department  ,tbl.ename as Employee ,   tbl.salary  as Salary  from 
(

select e.salary as salary ,d.name as dname ,e.name as ename ,dense_rank() over(partition by d.name order by e.salary desc) as rnk
from Employee e
left join Department d
on e.departmentId = d.id
) tbl
where tbl.rnk <=3;

