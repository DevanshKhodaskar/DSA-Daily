# Write your MySQL query statement below
select DATE_FORMAT(trans_date, '%Y-%m') as month,country ,
        count(*) as trans_count, 
        SUM(CASE WHEN state='approved' THEN 1 ELSE 0 END) as approved_count  
        ,SUM(amount) as trans_total_amount  
        ,SUM(CASE when state = "approved" then amount else 0 END) as approved_total_amount 

from Transactions
GROUP BY DATE_FORMAT(trans_date, '%Y-%m'), country;