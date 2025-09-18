import numpy as np
import pandas as pd
import statsmodels.api as sm
import os

### STEP 1. Creating a raw dataset with some missing values and outliers ###

# Create a folder to store a dataset (with some missing values and outliers)
os.makedirs('data', exist_ok=True)

# Generating synthethic dataset
np.random.seed(42)

n = 500
x = np.random.normal(50, 10, n)                 # independent variable
y = 3 + 2*x + np.random.normal(0, 10, n)        # dependent variable with noise 

df_raw = pd.DataFrame({'x': x, 'y': y})

# Introducing missing values to the dataset
missing_idx = np.random.choice(df_raw.index, size = int(0.05*n), replace = False)
df_raw.loc[missing_idx, 'y'] = np.nan

# Adding some outliers to the dataset
outlier_idx = np.random.choice(df_raw.index, size = 5, replace=True)
df_raw.loc[outlier_idx, 'y'] = df_raw.loc[outlier_idx, 'y']*10

# Saving the raw dataset
df_raw.to_csv('data/raw_data.csv', index = False)



### STEP 2. Cleaning the raw dataset ###
df = df_raw.dropna() # remove the missing values
df = df[df['y'] < df['y'].quantile(0.99)] # drop top 1 % outliers

# Save the cleaned dataset
os.makedirs('outputs', exist_ok=True)
df.to_csv('outputs/cleaned_data.csv', index = False)

### STEP 3. Make regression analysis using statsmodels.api 

X = sm.add_constant(df['x']) # add the intercept
y = df['y']

model = sm.OLS(y, X).fit()

print(model.summary())

# Same summary to .txt file
with open('outputs/regression_summary', 'w') as f:
    f.write(model.summary().as_text())


