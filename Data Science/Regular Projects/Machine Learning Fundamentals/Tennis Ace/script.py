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

#Familiarised myself with data, interested in Winnings, and win RATE, more importantly, so I'll have to make another column with each players winrate and treat that as a target variable.

df['winrate'] = (df['Wins'] / (df['Wins'] + df['Losses'])) * 100

#strange, NaN show up when observing new winrate column. 


