import pandas as pd
data = { 'Name': [' Alice ', 'bob', 'CHARLIE', 'david*', None],  'Email': ['alice@example.com ', 'BOB@EXAMPLE.COM', 'charlie@example.COM', 'david#@example.com', 'eve@example.com']}
df = pd.DataFrame(data)
df['Name'] = df['Name'].str.strip()
df['Name'] = df['Name'].str.lower()
df['Name'] = df['Name'].str.replace('[^a-z ]', '', regex=True)
df['Email'] = df['Email'].str.strip().str.lower()
df['Name'].fillna('unknown', inplace=True)
print(df)
