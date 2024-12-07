import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned data
data_benin = pd.read_csv('../benin-malanville.csv')

# Boxplot to detect outliers in GHI
plt.figure(figsize=(8, 6))
sns.boxplot(data=data_benin, x='GHI')
plt.title("Outlier Detection in Benin GHI")
plt.show()
