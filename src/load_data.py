import pandas as pd


# Load the datasets
def load_data():
    try:
        # Read the solar data from CSVs
        data_benin = pd.read_csv('../../../assets/data/benin-malanville.csv')
        data_sierra_leone = pd.read_csv('../../../assets/data/sierraleone-bumbuna.csv')
        data_togo = pd.read_csv('../../../assets/data/togo-dapaong_qc.csv')

        # Preprocessing: Drop rows with invalid GHI values (negative GHI values make no sense)
        data_benin = data_benin[data_benin['GHI'] >= 0]
        data_sierra_leone = data_sierra_leone[data_sierra_leone['GHI'] >= 0]
        data_togo = data_togo[data_togo['GHI'] >= 0]

        # Handle missing temperature values
        data_benin['Tamb'] = data_benin['Tamb'].fillna(data_benin['Tamb'].mean())
        data_sierra_leone['Tamb'] = data_sierra_leone['Tamb'].fillna(data_sierra_leone['Tamb'].mean())
        data_togo['Tamb'] = data_togo['Tamb'].fillna(data_togo['Tamb'].mean())

        print("Data loaded and preprocessed successfully")
        return data_benin, data_sierra_leone, data_togo

    except Exception as e:
        print(f"Error while loading the data: {e}")
        return None, None, None


# Run the loader function
if __name__ == "__main__":
    benin, sierra_leone, togo = load_data()
    print(benin.head())
    print(sierra_leone.head())
    print(togo.head())
