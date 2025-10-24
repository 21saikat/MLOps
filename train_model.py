import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv('data/dataset.csv')

X = df[['feature1', 'feature2']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
import os
os.makedirs('app', exist_ok=True)
with open('app/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved!")

