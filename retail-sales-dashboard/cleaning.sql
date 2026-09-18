SELECT
    Order_ID,
    Order_Date,
    Region,
    Category,
    Sub_Category,
    Sales,
    Profit,
    Quantity,
    Discount
FROM retail_sales
WHERE Sales IS NOT NULL
  AND Profit IS NOT NULL;

