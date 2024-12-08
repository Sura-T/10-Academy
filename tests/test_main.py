import sys
import os

# Dynamically add the root directory to the Python path for testing
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app.main import load_data

# tests/test_main.py
from src.app.main import load_data

def test_load_data():
    data_benin, data_sierra_leone, data_togo = load_data()
    assert data_benin is not None, "Benin data should not be None"
    assert data_sierra_leone is not None, "Sierra Leone data should not be None"
    assert data_togo is not None, "Togo data should not be None"
