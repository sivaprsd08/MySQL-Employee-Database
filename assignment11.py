
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset("taxis")

print("TAXIS DATASET")
print(df.head())

print("\nDataset Information:")
print(df.info())


print("\nMissing Values Before Handling:")
print(df.isnull().sum())

# Convert pickup column into datetime format
df["pickup"] = pd.to_datetime(df["pickup"], errors="coerce")

# Remove rows where critical values are missing
df.dropna(subset=["pickup", "fare"], inplace=True)

# Identify numerical and categorical columns
numerical_columns = df.select_dtypes(include=np.number).columns

categorical_columns = df.select_dtypes(
    include=["object", "category"]
).columns

# Fill numerical missing values using median
for column in numerical_columns:
    df[column] = df[column].fillna(df[column].median())

# Fill categorical missing values using mode
for column in categorical_columns:
    if df[column].isnull().any():
        df[column] = df[column].fillna(df[column].mode()[0])

print("\nMissing Values After Handling:")
print(df.isnull().sum())

print("\nCleaned Dataset:")
print(df.head())


print("\nLine Chart")

df = df.sort_values("pickup")

plt.figure(figsize=(10, 5))

plt.plot(df["pickup"], df["fare"])

plt.title("Fare Over Time")
plt.xlabel("Pickup Timestamp")
plt.ylabel("Fare")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


print("\nBar Chart")

borough_fare = df.groupby("pickup_borough")["fare"].sum()

plt.figure(figsize=(8, 5))

borough_fare.plot(kind="bar")

plt.title("Total Fare by Pickup Borough")
plt.xlabel("Pickup Borough")
plt.ylabel("Total Fare")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


print("\nPie Chart")

payment_counts = df["payment"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    payment_counts,
    labels=payment_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Distribution of Trips by Payment Method")

plt.show()


print("\nHistogram")

plt.figure(figsize=(8, 5))

plt.hist(df["distance"], bins=20, edgecolor="black")

plt.title("Distribution of Trip Distance")
plt.xlabel("Distance")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()


print("\nBox Plot")

plt.figure(figsize=(9, 5))

df.boxplot(
    column="tip",
    by="pickup_borough"
)

plt.title("Distribution of Tips by Pickup Borough")
plt.suptitle("")
plt.xlabel("Pickup Borough")
plt.ylabel("Tip Amount")

plt.tight_layout()
plt.show()


print("\nCount Plot")

plt.figure(figsize=(9, 5))

sns.countplot(
    data=df,
    x="pickup_borough"
)

plt.title("Number of Trips by Pickup Borough")
plt.xlabel("Pickup Borough")
plt.ylabel("Number of Trips")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

print("\nScatter Plot")

plt.figure(figsize=(9, 5))

sns.scatterplot(
    data=df,
    x="distance",
    y="fare",
    hue="pickup_borough"
)

plt.title("Relationship Between Distance and Fare")
plt.xlabel("Distance")
plt.ylabel("Fare")

plt.tight_layout()
plt.show()

print("\nHeatmap")

numerical_data = df[
    ["distance", "fare", "tip", "tolls", "total"]
]

correlation_matrix = numerical_data.corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()

print("\nPair Plot")

pair_data = df[
    ["distance", "fare", "tip", "total", "pickup_zone"]
].copy()

# Select the five most common pickup zones
top_zones = pair_data["pickup_zone"].value_counts().head(5).index

pair_data = pair_data[
    pair_data["pickup_zone"].isin(top_zones)
]

sns.pairplot(
    pair_data,
    hue="pickup_zone"
)

plt.show()


print("\nViolin Plot")

plt.figure(figsize=(9, 5))

sns.violinplot(
    data=df,
    x="payment",
    y="fare"
)

plt.title("Fare Distribution by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Fare")

plt.tight_layout()
plt.show()


print("\n===================================")
print("ASSIGNMENT COMPLETED SUCCESSFULLY")
print("===================================")

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nAll Visualizations Completed!")
