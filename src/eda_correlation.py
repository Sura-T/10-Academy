import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load the dataset
data_benin = pd.read_csv('../benin-malanville.csv')

# Correlation analysis
plt.figure(figsize=(10, 8))
sns.heatmap(data_benin.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix for Benin")
plt.show()
