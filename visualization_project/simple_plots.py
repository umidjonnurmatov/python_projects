import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Generate synthetic data 
np.random.seed(42)
x = np.random.normal(50, 10, 500)
y = x*0.5 + np.random.normal(0, 5, 500)


df = pd.DataFrame({'x': x, 'y': y})

# Save the dataset
os.makedirs('data', exist_ok=True)


df.to_csv('data/sample_dataset.csv', index=False)

# Scatter plot
plt.figure(figsize = (8, 6))
sns.scatterplot(x = 'x', y = 'y', data = df, alpha = 0.7)
plt.title('Scatter Plot of x and y')
plt.show()



# Histogram
plt.figure(figsize = (8, 6))
sns.histplot(df['x'], bins = 20, kde = True, color = 'skyblue')
plt.title('Distribution of x')
plt.show()