import pandas as pd
import matplotlib.pyplot as plt


# Load the datasets
data_benin = pd.read_csv('../benin-malanville.csv')
data_sierra_leone = pd.read_csv('../sierraleone-bumbuna.csv')
data_togo = pd.read_csv('../togo-dapaong_qc.csv')


# Time-series plot for GHI over time
plt.figure(figsize=(10, 6))
plt.plot(pd.to_datetime(data_benin['Timestamp']), data_benin['GHI'], label="Benin GHI")
plt.plot(pd.to_datetime(data_sierra_leone['Timestamp']), data_sierra_leone['GHI'], label="Sierra Leone GHI")
plt.plot(pd.to_datetime(data_togo['Timestamp']), data_togo['GHI'], label="Togo GHI")
plt.xlabel('Timestamp')
plt.ylabel('Global Horizontal Irradiance (W/m²)')
plt.legend()
plt.title('GHI Over Time')
plt.show()
