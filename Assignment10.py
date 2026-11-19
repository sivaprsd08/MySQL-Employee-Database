import numpy as np
import pandas as pd

# Create Week 1 temperature array
temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])

print("Week 1 Temperatures:")
print(temperatures_w1)
print("Shape:", temperatures_w1.shape)

print("Data Type:", temperatures_w1.dtype)

print("Number of Elements:", temperatures_w1.size)
# Convert Celsius to Fahrenheit
temperatures_f = (temperatures_w1 * 9/5) + 32

print("Temperatures in Fahrenheit:")
print(temperatures_f)
# Maximum temperature
print("Maximum Temperature:", np.max(temperatures_w1))

# Minimum temperature
print("Minimum Temperature:", np.min(temperatures_w1))

# Mean temperature
print("Mean Temperature:", np.mean(temperatures_w1))
# First three days
print("First three days:", temperatures_w1[0:3])
# Weekend temperatures (last two days)
print("Weekend Temperatures:", temperatures_w1[-2:])
# Middle three days
print("Middle Three Days:", temperatures_w1[2:5])
# Create a 2D array for two weeks

temperatures = np.array([
    [22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9],
    [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1]
])

print("Temperatures for Two Weeks:")
print(temperatures)
print("Shape:", temperatures.shape)
print("Data Type:", temperatures.dtype)
print("Number of Elements:", temperatures.size)
print("Week 1 Temperatures:", temperatures[0])
print("Week 2 Temperatures:", temperatures[1])
print("Weekend Temperatures for Both Weeks:")
print(temperatures[:, -2:])
# Create a Pandas Series

marks = pd.Series(
    [85, 90, 78, 92, 88],
    index=["Rank1", "Rank2", "Rank3", "Rank4", "Rank5"]
)

print("Student Marks:")
print(marks)
# Access elements using integer position

print("First Student Marks:", marks.iloc[0])
print("Third Student Marks:", marks.iloc[2])
# Access elements using index labels

print("Marks of Rank2:", marks.loc["Rank2"])
print("Marks of Rank4:", marks.loc["Rank4"])
# Filter students scoring more than 85

print("Students scoring above 85:")
print(marks[marks > 85])
# Modify the marks of Rank1

marks.loc["Rank1"] = 100

print("Updated Student Marks:")
print(marks)
# Remove Rank5

marks = marks.drop("Rank5")

print("Series after removing Rank5:")
print(marks)
# Calculate CGPA

cgpa = marks / 10

print("Student CGPA:")
print(cgpa)
# Create a Pandas DataFrame

transactions = pd.DataFrame({
    "TransactionID": [101, 102, 103, 104, 105, 106, 107, 108, 109],
    "ProductCategory": ["Electronics", "Clothing", "Groceries", "Electronics", "Clothing", "Groceries", "Electronics", "Clothing", "Groceries"],
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West", "North"],
    "Amount": [250, 180, 120, 300, 220, 150, 400, 190, 280]
})

print("Sales Transactions:")
print(transactions)
# Display first five rows

print("First Five Rows:")
print(transactions.head())

# Display last five rows

print("Last Five Rows:")
print(transactions.tail())
# Check DataFrame properties

print("Shape:", transactions.shape)
print("Column Names:", transactions.columns)
print("Data Types:")
print(transactions.dtypes)
# Select a single column

print("Transaction Amounts:")
print(transactions["Amount"])

# Select multiple columns

print("Transaction ID and Region:")
print(transactions[["TransactionID", "Region"]])
# Select the last three columns

print("Last Three Columns:")
print(transactions.iloc[:, -3:])
# Filter transactions from North region

print("Transactions from North Region:")
print(transactions[transactions["Region"] == "North"])

# Filter transactions with Amount greater than 200

print("Transactions with Amount above 200:")
print(transactions[transactions["Amount"] > 200])
# Count product categories

print("Product Category Counts:")
print(transactions["ProductCategory"].value_counts())
# Find unique regions

print("Unique Regions:")
print(transactions["Region"].unique())
# Calculate average amount by region

print("Average Transaction Amount by Region:")
print(transactions.groupby("Region")["Amount"].mean())
# Modify transaction amount

transactions.loc[transactions["TransactionID"] == 102, "Amount"] = 165

print("Updated Transactions:")
print(transactions)
# Add Discount column

transactions["Discount"] = transactions["Amount"] * 0.10

print("Transactions with Discount:")
print(transactions)
# Remove transaction ID 109

transactions = transactions.drop(
    transactions[transactions["TransactionID"] == 109].index
)

print("Transactions after removing ID 109:")
print(transactions)
# Delete Discount column

del transactions["Discount"]

print("Final Transactions DataFrame:")
print(transactions)
