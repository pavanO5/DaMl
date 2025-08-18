import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\pavan\Downloads\IRIS (1).csv")
df.head(10)
df.info()

#Missing values Handling
for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        df[col].fillna(df[col].median(), inplace=True)
    else:
        df[col].fillna(df[col].mode()[0], inplace=True)
print("Missing values after filling:\n", df.isnull().sum())

#Handling Duplicate Values
duplicate_count = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_count}")
df.drop_duplicates(inplace=True)
print(f"Data shape after removing duplicates: {df.shape}")

#Handling Null Values
print("Null values before dropping:\n", df.isnull().sum())
df.dropna(inplace=True)
print(f"Shape after dropping nulls: {df.shape}")
print("Null values after dropping:\n", df.isnull().sum())

#Handling Outliers
Q1 = df['SepalLengthCm'].quantile(0.25)
Q3 = df['SepalLengthCm'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[(df['SepalLengthCm'] >= lower_bound) & (df['SepalLengthCm'] <= upper_bound)]
print(f"Data shape after removing outliers: {df.shape}")

#Final cleaned data
print(df.head())


