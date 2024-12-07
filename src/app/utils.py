import pandas as pd


def load_data():
    """
    Function to load all environmental datasets.
    Returns processed data for Benin, Sierra Leone, and Togo.
    """
    try:
        data_benin = pd.read_csv('../../benin-malanville.csv')
        data_sierra_leone = pd.read_csv('../../sierraleone-bumbuna.csv')
        data_togo = pd.read_csv('../../togo-dapaong_qc.csv')
        return data_benin, data_sierra_leone, data_togo
    except Exception as e:
        print(f"Error loading datasets: {e}")
        return None, None, None
