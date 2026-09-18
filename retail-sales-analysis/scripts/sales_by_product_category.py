import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales_dataset.csv")

category_sales = df.groupby('Product Category')['Total Amount'].sum().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=category_sales, x='Product Category', y='Total Amount')

plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales ($)")
plt.tight_layout()
plt.show()
