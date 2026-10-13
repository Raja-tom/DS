import pandas as pd
import numpy as np
from scipy import stats
df = pd.read_csv('raw_data.csv')  # Replace with your filename
print("Initial Data Summary:")
print(df.info())
print("\nMissing Values:\n", df.isnull().sum())
for col in df.columns:
    if df[col].dtype in ['float64', 'int64']:
        df[col].fillna(df[col].mean(), inplace=True)
    else:
        df[col].fillna(df[col].mode()[0], inplace=True)
df.drop_duplicates(inplace=True)
text_cols = df.select_dtypes(include='object').columns
for col in text_cols:
    df[col] = df[col].str.strip().str.lower()
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
if 'price' in df.columns:
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
if 'status' in df.columns:
    df['status'] = df['status'].map({
        'active': 'active',
        'inactive': 'inactive',
        'in-active': 'inactive',
        'actve': 'active'
    })
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
for col in numeric_cols:
    df = df[(np.abs(stats.zscore(df[col])) < 3)]
print("\nCleaned Data Summary:")
print(df.info())
df.to_csv('cleaned_data.csv', index=False)
print("\nCleaned data saved as 'cleaned_data.csv'")
