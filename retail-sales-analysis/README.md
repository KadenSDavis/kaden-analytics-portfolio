# Retail Sales Analysis

## Project Overview

This project analyzes retail transaction data using Python to identify sales trends, customer purchasing patterns, and product category performance.

The goal of this analysis is to transform raw retail transaction data into meaningful business insights using data cleaning, exploratory data analysis, and visualization.

## Key Metrics

| Metric | Value |
|---|---:|
| Total Revenue | $456,000 |
| Total Transactions | 1,000 |
| Average Transaction Value | $456 |
| Total Units Sold | 2,514 |

## Business Questions

This analysis explores the following questions:

- How do sales change over time?
- Which product categories generate the most revenue?
- How do sales vary across product categories over time?
- Which age groups contribute the most to sales?
- Is there a relationship between quantity purchased and transaction value?

## Dataset

The dataset contains retail transaction information, including:

- Transaction ID
- Date
- Customer ID
- Gender
- Age
- Product Category
- Quantity
- Price per Unit
- Total Amount

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter/PyCharm
- GitHub

## Analysis & Visualizations

### Monthly Sales Trend

Analyzes how total sales change over time.

![Monthly Sales Trend](visualizations/Monthly%20Sales%20Trend%20%28Line%20Chart%29.png)

### Monthly Sales by Product Category

Shows how sales for each product category change over time.

![Monthly Sales by Product Category](visualizations/Monthly%20Sales%20by%20Product%20Category.png)

### Sales by Product Category

Compares total sales across product categories.

![Sales by Product Category](visualizations/Sales%20by%20Product%20Category.png)

### Revenue Share by Product Category

Shows the contribution of each product category to total revenue.

![Revenue Share by Product Category](visualizations/Revenue%20Share%20by%20Product%20Category.png)

### Total Sales by Age Group

Examines total sales across different customer age groups.

![Total Sales by Age Group](visualizations/Total%20Sales%20By%20Age%20Group.png)

### Quantity vs. Total Amount

Explores the relationship between quantity purchased and transaction value.

![Quantity vs Total Amount](visualizations/Quantity%20vs%20Total%20Amount.png)

## Key Findings

- The dataset contains 1,000 retail transactions generating $456,000 in total sales.
- Electronics generated $156,905 in sales, followed by Clothing at $155,580 and Beauty at $143,515.
- Electronics accounted for approximately 34.4% of total revenue.
- Clothing accounted for approximately 34.1% of total revenue.
- Beauty accounted for approximately 31.5% of total revenue.
- The average transaction value was $456.
- A total of 2,514 units were sold across the dataset.

## Project Structure

```text
retail-sales-analysis/
│
├── README.md
│
├── data/
│   └── retail_sales_dataset.csv
│
├── scripts/
│   ├── monthly_sales_by_category.py
│   ├── monthly_sales_trend.py
│   ├── quantity_vs._total_amount.py
│   ├── revenue_share_by_category.py
│   ├── sales_by_age_group.py
│   └── sales_by_product_category.py
│
├── visualizations/
│   ├── monthly_sales_trend.png
│   ├── monthly_sales_by_product_category.png
│   ├── quantity_vs._total_amount.png
│   ├── revenue_share_by_product_category.png
│   ├── sales_by_product_category.png
│   └── total_sales_by_age_group.png
│
└── requirements.txt
