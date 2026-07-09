import pandas as pd
import numpy as np

print(df.head())

# for missing issues 
print("\nShape:", df.shape)
print("\nNaN counts:\n", df.isnull().sum()[df.isnull().sum() > 0])

for col in df.select_dtypes(include='object').columns:
    blanks = df[col].astype(str).str.strip().eq('').sum()
    if blanks > 0:
        print(f"{col}: {blanks} blank values")

# ---- Clean ----

#  Strip whitespace from all text columns
str_cols = df.select_dtypes(include='object').columns
for col in str_cols:
    df[col] = df[col].str.strip()

     
