import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
data = {
    'Hours_Studied': [1, 2, 3, 4.5, 5, 6, 7.5, 8, 9, 10],
    'Scores': [35, 40, 50, 60, 65, 70, 80, 85, 90, 95]
}
df = pd.DataFrame(data)
X = df[['Hours_Studied']]
y = df['Scores']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Actual vs Predicted:")
print(pd.DataFrame({'Actual': y_test, 'Predicted': y_pred}))
print("\nMean Squared Error:", mse)
print("R2 Score (Accuracy):", r2)
