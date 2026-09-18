import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales_dataset.csv")

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M').astype(str)

monthly = df.groupby('Month')['Total Amount'].sum().reset_index()

plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly, x='Month', y='Total Amount', marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("monthly_trend.png")
plt.show()