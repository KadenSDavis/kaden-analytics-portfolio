import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales_dataset.csv")

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create Month column
df['Month'] = df['Date'].dt.to_period('M').astype(str)

# Calculate monthly sales by category
monthly_category = (
    df.groupby(['Month', 'Product Category'])['Total Amount']
    .sum()
    .reset_index()
)

# Create chart
plt.figure(figsize=(12, 6))

sns.lineplot(
    data=monthly_category,
    x='Month',
    y='Total Amount',
    hue='Product Category',
    marker='o'
)

plt.title("Monthly Sales by Product Category")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()