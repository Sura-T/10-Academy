import pandas as pd

# Load datasets from the root directory
data_benin = pd.read_csv('../benin-malanville.csv')
data_sierra_leone = pd.read_csv('../sierraleone-bumbuna.csv')
data_togo = pd.read_csv('../togo-dapaong_qc.csv')

# Display basic info about each daartaset
print("Benin Data Info:")
print(data_benin.info())

print("\nSierra Leone Data Info:")
print(data_sierra_leone.info())

print("\nTogo Data Info:")
print(data_togo.info())

# Display the first few rows from each dataset
print("\nFirst 5 Rows of Benin Data:")
print(data_benin.head())

print("\nFirst 5 Rows of Sierra Leone Data:")
print(data_sierra_leone.head())

print("\nFirst 5 Rows of Togo Data:")
print(data_togo.head())


# Summary statistics for Benin data
print("\nSummary Statistics for Benin Data:")
print(data_benin.describe())

# Summary statistics for Sierra Leone data
print("\nSummary Statistics for Sierra Leone Data:")
print(data_sierra_leone.describe())

# Summary statistics for Togo data
print("\nSummary Statistics for Togo Data:")
print(data_togo.describe())


# Missing value analysis for each dataset
print("\nMissing Values in Benin Data:")
print(data_benin.isnull().sum())

print("\nMissing Values in Sierra Leone Data:")
print(data_sierra_leone.isnull().sum())

print("\nMissing Values in Togo Data:")
print(data_togo.isnull().sum())



# Remove rows where GHI is negative
data_benin = data_benin[data_benin['GHI'] >= 0]
data_sierra_leone = data_sierra_leone[data_sierra_leone['GHI'] >= 0]
data_togo = data_togo[data_togo['GHI'] >= 0]

# Fill missing temperature values with the mean
data_benin['Tamb'] = data_benin['Tamb'].fillna(data_benin['Tamb'].mean())
data_sierra_leone['Tamb'] = data_sierra_leone['Tamb'].fillna(data_sierra_leone['Tamb'].mean())
data_togo['Tamb'] = data_togo['Tamb'].fillna(data_togo['Tamb'].mean())
