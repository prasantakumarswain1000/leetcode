# Write your MySQL query statement below
-- Case 1: Products that DID have a price change before Aug 16
SELECT product_id, new_price AS price
FROM Products
WHERE (product_id, change_date) IN (
    SELECT product_id, MAX(change_date)
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)

UNION

-- Case 2: Products that did NOT have any price change before Aug 16
SELECT product_id, 10 AS price
FROM Products
WHERE product_id NOT IN (
    SELECT product_id FROM Products WHERE change_date <= '2019-08-16'
);