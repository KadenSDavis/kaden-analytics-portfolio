import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales_dataset.csv")

df['Age Group'] = pd.cut(
    df['Age'],
    bins=[17, 24, 34, 44, 54, 64],
    labels=['18-24', '25-34', '35-44', '45-54', '55-64']
)

age_sales = df.groupby('Age Group', observed=True)['Total Amount'].sum().reset_index()

plt.figure(figsize=(9, 5))
sns.barplot(data=age_sales, x='Age Group', y='Total Amount')

plt.title("Total Sales by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Sales ($)")
plt.tight_layout()
plt.show()