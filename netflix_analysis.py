import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")

# Data Cleaning
df = df.dropna(subset=["country", "rating"])

# Most common content type
print(df["type"].value_counts())

# Top countries
top_countries = df["country"].value_counts().head(10)
print(top_countries)

# Visualization
top_countries.plot(kind="bar")
plt.title("Top Countries Producing Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()

# Content over years
df["year_added"] = pd.to_datetime(df["date_added"]).dt.year
df["year_added"].value_counts().sort_index().plot()

plt.title("Content Added Over Years")
plt.show()