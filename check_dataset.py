import pandas as pd

df = pd.read_csv("dataset/train.csv")

print("First 5 Rows:")
print(df.head())

print("\nColumns:")
print(df.columns.tolist())

print("\nShape:")
print(df.shape)