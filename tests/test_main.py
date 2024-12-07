import pytest
from src.app.main import load_data  # Import the function to test


def test_load_data():
    data = load_data()
    assert data is not None  # Add proper checks depending on your logic
