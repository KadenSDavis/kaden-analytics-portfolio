SELECT
    Region,
    Category,
    Sales,
    SUM(Sales) OVER (PARTITION BY Region) AS Regional_Sales,
    RANK() OVER (PARTITION BY Region ORDER BY Sales DESC) AS Regional_Rank
FROM retail_sales;

