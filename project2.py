import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load data
data = pd.read_csv("data.csv")

X = data[["Hours"]]
y = data["Pass"]

# Train model
model = LogisticRegression()
model.fit(X, y)

print("Model trained successfully!")

# Prediction
hours = int(input("Enter study hours: "))
result = model.predict([[hours]])

if result[0] == 1:
    print("Pass")
else:
    print("Fail")
