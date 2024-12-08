import pandas as pd
import os


# Load the datasets
def load_data():
    try:
        # Dynamically resolve paths using the current directory
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Dynamically resolve the path
        data_benin = pd.read_csv(os.path.join(base_dir, "../assets/data/benin-malanville.csv"))
        data_sierra_leone = pd.read_csv(os.path.join(base_dir, "../assets/data/sierraleone-bumbuna.csv"))
        data_togo = pd.read_csv(os.path.join(base_dir, "../assets/data/togo-dapaong_qc.csv"))

        # Preprocessing: Drop invalid GHI values and handle missing temperature data
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
