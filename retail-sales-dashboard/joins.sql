SELECT
    r.Order_ID,
    r.Order_Date,
    r.Region,
    r.Category,
    r.Sub_Category,
    r.Sales,
    r.Profit,
    c.Customer_Name
FROM retail_sales r
LEFT JOIN customers c
    ON r.Customer_ID = c.Customer_ID;

