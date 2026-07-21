

select stock_name,sum(if(operation='Sell',price,-price)) as capital_gain_loss
from stocks
group by stock_name;
 # Write your MySQL query statement below
# select stock_name ,sum(case when operation='Sell' then price else -price end) as capital_gain_loss
# from stocks 
# group by stock_name;