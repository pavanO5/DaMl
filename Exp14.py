import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\pavan\Downloads\IRIS (1).csv")
df.head(10)
df.info()

#Normalization Technique
from sklearn.preprocessing import MinMaxScaler
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
scaler = MinMaxScaler()
df_normalized = df.copy()
df_normalized[numeric_cols] = scaler.fit_transform(df[numeric_cols])
print("\n--- Normalized Data (First 5 rows) ---")
print(df_normalized[numeric_cols].head())

#Scaling Technique
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
df_scaled = df.copy()
df_scaled[numeric_cols] = scaler.fit_transform(df[numeric_cols])
print("\n--- Scaled Data (First 5 rows) ---")
print(df_scaled[numeric_cols].head())

#Standardization Technique
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df_standardized = df.copy()
df_standardized[numeric_cols] = scaler.fit_transform(df[numeric_cols])
print("\n--- Standardized Data (First 5 rows) ---")
print(df_standardized[numeric_cols].head())

