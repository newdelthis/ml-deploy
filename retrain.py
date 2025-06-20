import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("data/training.csv")
X = df[['YearsExperience']]
y = df['Salary']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)
