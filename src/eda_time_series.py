import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
data_benin = pd.read_csv('../benin-malanville.csv')
data_sierra_leone = pd.read_csv('../sierraleone-bumbuna.csv')
data_togo = pd.read_csv('../togo-dapaong_qc.csv')

# Plot GHI over time for each dataset
plt.figure(figsize=(10, 6))
plt.plot(pd.to_datetime(data_benin['Timestamp']), data_benin['GHI'], label="Benin GHI")
plt.plot(pd.to_datetime(data_sierra_leone['Timestamp']), data_sierra_leone['GHI'], label="Sierra Leone GHI")
plt.plot(pd.to_datetime(data_togo['Timestamp']), data_togo['GHI'], label="Togo GHI")
plt.xlabel('Timestamp')
plt.ylabel('Global Horizontal Irradiance (GHI)')
plt.title('GHI Over Time')
plt.legend()
plt.show()
