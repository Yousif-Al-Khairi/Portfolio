import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Data Science\Regular Projects\Machine Learning Fundamentals\Tennis Ace\Tennis_stats.csv")

print(df.head())
print("------------------------------------------")
print(df.columns)
print("------------------------------------------")
print(df.dtypes)
print("------------------------------------------")

#Familiarised myself with data, interested in Winnings, and win RATE, more importantly, so I'll have to make another column with each players winrate and treat that as a target variable.

df['winrate'] = (df['Wins'] / (df['Wins'] + df['Losses'])) * 100
print(df["winrate"])
print("------------------------------------------")
nan_count = df["winrate"].isna().sum()
print("Number of NaNs:", nan_count)
print("------------------------------------------")

#strange, NaN show up when observing new winrate column. 

#print(df['Wins'].hasnans)
#print(df['Losses'].hasnans)

# What is causing NaNs when calculating winrate column is probably trying to divide by 0 in the case that a player has no matches played (no wins or losses)


