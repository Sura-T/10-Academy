import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load the dataset
data_benin = pd.read_csv('../benin-malanville.csv')


# Visualize outliers using boxplots
plt.figure(figsize=(8, 6))
sns.boxplot(x=data_benin['GHI'])
plt.title("Outlier Detection in Benin GHI")
plt.show()
