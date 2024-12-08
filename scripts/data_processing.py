import pandas as pd

def load_and_clean_data(file_path):
    """Load and preprocess data."""
    try:
        # Load CSV
        data = pd.read_csv(file_path)

        # Preprocessing: Remove invalid or missing data
        data = data[data['GHI'] >= 0]  # Remove negative GHI values
        data['Tamb'] = data['Tamb'].fillna(data['Tamb'].mean())  # Handle missing temperatures

        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
