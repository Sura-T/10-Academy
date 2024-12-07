import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
data_benin = pd.read_csv('../benin-malanville.csv')
data_sierra_leone = pd.read_csv('../sierraleone-bumbuna.csv')
data_togo = pd.read_csv('../togo-dapaong_qc.csv')

# Scatter plot of GHI vs Wind Speed
plt.figure(figsize=(8, 6))
plt.scatter(data_benin['WS'], data_benin['GHI'], alpha=0.5, label="Benin")
plt.scatter(data_sierra_leone['WS'], data_sierra_leone['GHI'], alpha=0.5, label="Sierra Leone")
plt.scatter(data_togo['WS'], data_togo['GHI'], alpha=0.5, label="Togo")
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Global Horizontal Irradiance (GHI)')
plt.title('GHI vs Wind Speed')
plt.legend()
plt.show()
