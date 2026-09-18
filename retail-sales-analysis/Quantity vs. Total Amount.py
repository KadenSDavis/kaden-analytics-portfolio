import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales_dataset.csv")

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x='Quantity',
    y='Total Amount'
)

plt.title("Quantity vs. Total Amount")
plt.xlabel("Quantity")
plt.ylabel("Total Amount ($)")
plt.tight_layout()
plt.show()