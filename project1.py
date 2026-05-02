import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("students.csv")

# Average marks
avg = data["Marks"].mean()

# Topper
topper = data.loc[data["Marks"].idxmax()]

print("Average Marks:", avg)
print("Topper:", topper["Name"], "-", topper["Marks"])

# Bar graph
plt.bar(data["Name"], data["Marks"])
plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
