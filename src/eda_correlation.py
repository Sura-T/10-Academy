import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned data
data_benin = pd.read_csv('../benin-malanville.csv')

# Select only numeric columns
numeric_data_benin = data_benin.select_dtypes(include=['float64', 'int64'])

# Correlation matrix for numeric columns only
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_data_benin.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix for Benin Data")
plt.show()
