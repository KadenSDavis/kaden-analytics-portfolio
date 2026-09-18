import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales_dataset.csv")

category_sales = df.groupby('Product Category')['Total Amount'].sum()

plt.figure(figsize=(7, 7))
plt.pie(
    category_sales,
    labels=category_sales.index,
    autopct='%1.1f%%'
)

plt.title("Revenue Share by Product Category")
plt.show()