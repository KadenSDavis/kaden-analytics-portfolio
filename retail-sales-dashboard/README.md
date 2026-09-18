Retail Sales Performance Dashboard — Power BI + SQL
A business intelligence dashboard analyzing retail sales, profitability, and product performance across regions. Built using Power BI, DAX, and SQL, with a star‑schema data model and KPI‑driven insights.

📌 Project Overview
Retail companies need fast, accurate visibility into sales trends, profitability, and product performance. This dashboard provides a clear, interactive view of:

Monthly sales performance
Regional revenue distribution
Profitability by category
Top‑performing products
Discount impact on profit
The project demonstrates end‑to‑end BI development: data cleaning, SQL analysis, modeling, DAX measures, and dashboard design.

🧠 Business Questions Answered
Which regions generate the most revenue?
Which product categories drive profit?
What are the top 10 products by sales?
How do discounts affect profitability?
What are the month‑over‑month sales trends?

🗂 Dataset
Source: Kaggle Retail Sales Dataset
Rows: ~10,000
Columns include:
Order Date
Region
Category
Sub‑Category
Sales
Profit
Quantity
Discount

🧩 Data Model (Star Schema)
Fact Table:
  FactSales (Sales, Profit, Quantity, Discount, Category, Sub‑Category, Region, Order Date)
Dimension Tables:
DimDate
DimProduct
DimRegion

This structure supports flexible slicing, filtering, and KPI calculations.

📐 DAX Measures
Total Sales = SUM(FactSales[Sales])
Total Profit = SUM(FactSales[Profit])
Profit Margin % = DIVIDE([Total Profit], [Total Sales])
Sales YoY = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(DimDate[Date]))

🧮 SQL Analysis
Folder: /sql/

Includes:

cleaning.sql
Basic data cleaning and null handling.

joins.sql
Joining sales with customer/product tables.

window_functions.sql
Ranking products by regional sales using window functions.

📊 Dashboard Visuals
KPI Cards: Total Sales, Total Profit, Profit Margin %
Monthly Sales Trend: Line chart
Sales by Region: Bar chart
Profit by Category: Bar chart
Top 10 Products: Sorted bar chart
Discount Impact: Scatter plot (Discount vs Profit)

🛠 Tech Stack
Power BI
DAX
SQL
Star‑schema modeling
Data cleaning & transformation
KPI design

🎯 Key Outcomes
Identified top‑performing regions and categories
Highlighted discount patterns that reduce profit
Revealed monthly sales trends for forecasting
Created a reusable BI model for future dashboards
