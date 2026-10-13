import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {
    'vs_currency': 'usd',
    'days': '1',
    'interval': 'hourly'
}
response = requests.get(url, params=params)
data = response.json()
prices = data['prices']
df = pd.DataFrame(prices, columns=['Timestamp', 'Price'])
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='ms')
print("Latest Price:", df['Price'].iloc[-1])
print("Max Price:", df['Price'].max())
print("Min Price:", df['Price'].min())
print("Average Price:", df['Price'].mean())
plt.figure(figsize=(10, 5))
plt.plot(df['Timestamp'], df['Price'], marker='o', linestyle='-')
plt.title('Bitcoin Price (Last 24 Hours)')
plt.xlabel('Time')
plt.ylabel('Price in USD')
plt.grid(True)
plt.tight_layout()
plt.show()
