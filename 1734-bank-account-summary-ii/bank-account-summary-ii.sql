select u.name,sum(tra.amount) as  balance
from Users u
join Transactions tra
on u.account=tra.account
group by tra.account,u.name
having balance>10000;
