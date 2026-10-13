import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
arr = np.array([10, 20, 30, 40])
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Marks': [85, 90, 78]}
df = pd.DataFrame(data)
print(df)
print("Average Marks:", df['Marks'].mean())
plt.plot([1, 2, 3], [10, 20, 30])
plt.title("Simple Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
sns.barplot(x='Name', y='Marks', data=df)
plt.title("Marks of Students")
plt.show()
