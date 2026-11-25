# SOCIAL MEDIA ENGAGEMENT ANALYTICS
# Data Analytics - Module End Assignment 5


# 1. IMPORTING LIBRARIES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# 2. IMPORTING DATASET

df = pd.read_csv(r"C:\Users\kpe00\Downloads\social_media_engagement_5000.csv")

print("\nFIRST FIVE ROWS")
print(df.head())

print("\nLAST FIVE ROWS")
print(df.tail())

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns)

print("\nDATASET INFORMATION")
df.info()


# 3. CHECKING MISSING VALUES

print("\nMISSING VALUES IN EACH COLUMN")
print(df.isnull().sum())

print("\nTOTAL MISSING VALUES")
print(df.isnull().sum().sum())


# 4. CHECKING DUPLICATE VALUES

print("\nNUMBER OF DUPLICATES")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nSHAPE AFTER REMOVING DUPLICATES")
print(df.shape)


# 5. DATA CLEANING

# Converting numeric columns into proper numeric format

numeric_columns = ["age", "likes", "comments", "shares",
                   "watch_time_sec", "impression_count",
                   "follower_count", "engagement_rate"]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")


# Replacing unrealistic negative values with missing values

for column in ["age", "likes", "comments", "shares",
               "watch_time_sec", "impression_count",
               "follower_count", "engagement_rate"]:

    df.loc[df[column] < 0, column] = np.nan


# Filling missing numeric values with median

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())


# Filling missing categorical values with mode

categorical_columns = ["gender", "country", "post_type",
                       "post_category", "device_type", "sentiment"]

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])


# Standardizing text values

for column in categorical_columns:
    df[column] = df[column].astype(str).str.strip().str.lower()


# Checking age values

df.loc[(df["age"] < 13) | (df["age"] > 100), "age"] = df["age"].median()


# Converting date column into datetime format

df["posted_at"] = pd.to_datetime(
    df["posted_at"], format="%d-%m-%Y", errors="coerce"
)


# Filling missing dates using forward fill

df["posted_at"] = df["posted_at"].ffill()
df["posted_at"] = df["posted_at"].bfill()


# Checking missing values after cleaning

print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())


# 6. FEATURE CREATION

# Creating engagement score

df["engagement_score"] = (
    df["likes"] + df["comments"] + df["shares"]
)


# Counting hashtags in each post

df["hashtag_count"] = df["hashtags"].fillna("").apply(
    lambda x: len(x.split())
)


# Creating log transformed columns

df["log_likes"] = np.log1p(df["likes"])
df["log_comments"] = np.log1p(df["comments"])
df["log_shares"] = np.log1p(df["shares"])


# Extracting day from posted date

df["posted_day"] = df["posted_at"].dt.date


# 7. EXPLORATORY DATA ANALYSIS

print("\nDATASET AFTER CLEANING")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nDATA TYPES")
print(df.dtypes)

print("\nSUMMARY STATISTICS")
print(df.describe())


# Checking unique values

print("\nGENDER DISTRIBUTION")
print(df["gender"].value_counts())

print("\nPOST TYPE DISTRIBUTION")
print(df["post_type"].value_counts())

print("\nPOST CATEGORY DISTRIBUTION")
print(df["post_category"].value_counts())

print("\nSENTIMENT DISTRIBUTION")
print(df["sentiment"].value_counts())

print("\nCOUNTRIES")
print(df["country"].unique())

print("\nNUMBER OF DIFFERENT COUNTRIES")
print(df["country"].nunique())


# 8. GROUPBY ANALYSIS

print("\nAVERAGE LIKES BY POST TYPE")

post_type_analysis = df.groupby("post_type")["likes"].mean()
print(post_type_analysis)


print("\nAVERAGE ENGAGEMENT BY POST CATEGORY")

category_analysis = df.groupby("post_category")[
    "engagement_score"
].mean()

print(category_analysis)


print("\nAVERAGE ENGAGEMENT RATE BY COUNTRY")

country_analysis = df.groupby("country")[
    "engagement_rate"
].mean().sort_values(ascending=False)

print(country_analysis)


print("\nAVERAGE WATCH TIME BY DEVICE")

device_analysis = df.groupby("device_type")[
    "watch_time_sec"
].mean()

print(device_analysis)


print("\nAVERAGE ENGAGEMENT RATE BY SENTIMENT")

sentiment_analysis = df.groupby("sentiment")[
    "engagement_rate"
].mean()

print(sentiment_analysis)


# 9. STATISTICAL ANALYSIS

columns_for_statistics = [
    "likes",
    "comments",
    "shares",
    "watch_time_sec",
    "engagement_rate",
    "follower_count"
]

print("\nSTATISTICAL ANALYSIS")

for column in columns_for_statistics:

    print("\nStatistics for", column)

    print("Mean:", df[column].mean())
    print("Median:", df[column].median())
    print("Mode:", df[column].mode()[0])
    print("Standard Deviation:", df[column].std())
    print("Variance:", df[column].var())

    print("25th Percentile:", df[column].quantile(0.25))
    print("50th Percentile:", df[column].quantile(0.50))
    print("75th Percentile:", df[column].quantile(0.75))


# 10. CORRELATION MATRIX

correlation = df[columns_for_statistics + ["age"]].corr()

print("\nCORRELATION MATRIX")
print(correlation)


# 11. DATA VISUALIZATION USING MATPLOTLIB


# Plot 1 - Likes vs Impressions

plt.figure(figsize=(8, 5))

plt.scatter(df["impression_count"], df["likes"])

plt.xlabel("Impressions")
plt.ylabel("Likes")
plt.title("Likes vs Impressions")

plt.show()


# Plot 2 - Daily Engagement Trend

daily_engagement = df.groupby("posted_day")[
    "engagement_score"
].mean()

plt.figure(figsize=(10, 5))

plt.plot(daily_engagement.index, daily_engagement.values)

plt.xlabel("Date")
plt.ylabel("Average Engagement Score")
plt.title("Daily Engagement Trend")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# Plot 3 - Number of Posts by Category

category_count = df["post_category"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(category_count.index, category_count.values)

plt.xlabel("Post Category")
plt.ylabel("Number of Posts")
plt.title("Number of Posts by Category")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# Plot 4 - Gender Distribution

gender_count = df["gender"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    gender_count.values,
    labels=gender_count.index,
    autopct="%1.1f%%"
)

plt.title("Gender Distribution")

plt.show()


# Plot 5 - Age Distribution

plt.figure(figsize=(8, 5))

plt.hist(df["age"], bins=15, edgecolor="black")

plt.xlabel("Age")
plt.ylabel("Number of Users")
plt.title("Age Distribution")

plt.show()


# Plot 6 - Engagement Rate Box Plot

plt.figure(figsize=(8, 5))

plt.boxplot(df["engagement_rate"])

plt.ylabel("Engagement Rate")
plt.title("Distribution of Engagement Rate")

plt.show()


# 12. DATA VISUALIZATION USING SEABORN


# Plot 7 - Count Plot of Post Type

plt.figure(figsize=(8, 5))

sns.countplot(data=df, x="post_type")

plt.title("Number of Posts by Post Type")
plt.xlabel("Post Type")
plt.ylabel("Count")

plt.show()


# Plot 8 - Average Likes by Category

plt.figure(figsize=(9, 5))

sns.barplot(
    data=df,
    x="post_category",
    y="likes"
)

plt.title("Average Likes by Post Category")
plt.xlabel("Post Category")
plt.ylabel("Average Likes")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# Plot 9 - Followers vs Sentiment

plt.figure(figsize=(8, 5))

sns.violinplot(
    data=df,
    x="sentiment",
    y="follower_count"
)

plt.title("Follower Count by Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Followers")

plt.show()


# Plot 10 - Pair Plot

sample_data = df[
    ["age", "likes", "comments", "shares", "engagement_rate"]
].sample(min(500, len(df)), random_state=1)

sns.pairplot(sample_data)

plt.show()


# Plot 11 - Correlation Heatmap

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.show()


# Plot 12 - Engagement by Device

sample_data = df.sample(min(300, len(df)), random_state=1)

plt.figure(figsize=(8, 5))

sns.swarmplot(
    data=sample_data,
    x="device_type",
    y="engagement_rate"
)

plt.title("Engagement Rate by Device")
plt.xlabel("Device Type")
plt.ylabel("Engagement Rate")

plt.show()


# 13. INTERACTIVE VISUALIZATION USING PLOTLY


# Interactive Line Chart

fig1 = px.line(
    daily_engagement.reset_index(),
    x="posted_day",
    y="engagement_score",
    title="Daily Engagement Trend"
)

fig1.show()


# Interactive Bar Chart

fig2 = px.bar(
    category_analysis.reset_index(),
    x="post_category",
    y="engagement_score",
    title="Average Engagement by Category"
)

fig2.show()


# Interactive Scatter Plot

fig3 = px.scatter(
    df,
    x="impression_count",
    y="likes",
    color="post_type",
    title="Likes vs Impressions"
)

fig3.show()


# Interactive Bubble Chart

fig4 = px.scatter(
    df.sample(min(500, len(df)), random_state=1),
    x="likes",
    y="comments",
    size="shares",
    color="sentiment",
    hover_data=["post_type", "country"],
    title="Social Media Engagement Bubble Chart"
)

fig4.show()


# 14. FINAL INSIGHTS


print("\nFINAL INSIGHTS")


# Best performing post type

best_post_type = df.groupby("post_type")[
    "engagement_rate"
].mean().idxmax()

print("\nPost type with highest average engagement rate:",
      best_post_type)


# Best performing category

best_category = df.groupby("post_category")[
    "engagement_rate"
].mean().idxmax()

print("Best performing content category:", best_category)


# Country with highest engagement

best_country = df.groupby("country")[
    "engagement_rate"
].mean().idxmax()

print("Country with highest average engagement rate:",
      best_country)


# Age and engagement relationship

age_engagement = df.groupby("age")[
    "engagement_rate"
].mean()

print("\nAverage engagement rate by age")
print(age_engagement)


# Verified and non-verified account comparison

verified_analysis = df.groupby("is_verified")[
    "engagement_rate"
].mean()

print("\nEngagement rate of verified and non-verified accounts")
print(verified_analysis)


# Sentiment with highest engagement

best_sentiment = df.groupby("sentiment")[
    "engagement_rate"
].mean().idxmax()

print("\nSentiment with highest engagement:", best_sentiment)


# Device with highest watch time

best_device = df.groupby("device_type")[
    "watch_time_sec"
].mean().idxmax()

print("Device with highest average watch time:", best_device)


# Best time of day

print("\nBest time of day for impressions cannot be identified")
print("because the posted_at column contains only dates and")
print("does not contain the exact posting time.")


# 15. SAVING CLEANED DATASET

df.to_csv("cleaned_social_media_data.csv", index=False)

print("\nCleaned dataset saved successfully.")

print("\nASSIGNMENT COMPLETED")
