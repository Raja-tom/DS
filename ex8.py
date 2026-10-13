import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Sales': [150, 200, 250, 300, 400],
    'Profit': [50, 70, 80, 100, 130]
}
df = pd.DataFrame(data)
plt.figure(figsize=(8, 5))
plt.plot(df['Year'], df['Sales'], marker='o', label='Sales', color='blue')
plt.plot(df['Year'], df['Profit'], marker='s', label='Profit', color='green')
plt.title('Sales and Profit over Years')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.grid(True)
plt.show()
df.plot(x='Year', kind='bar', stacked=False, color=['skyblue', 'lightgreen'])
plt.title("Yearly Sales and Profit")
plt.ylabel("Amount")
plt.grid(axis='y')
plt.show()
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
