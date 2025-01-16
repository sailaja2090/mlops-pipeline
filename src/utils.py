import pandas as pd

def load_data(file_path):
    """Load the Iris dataset from a CSV file."""
    data = pd.read_csv(file_path)
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    return X, y
