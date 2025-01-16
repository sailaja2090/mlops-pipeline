import sys
import os
# Dynamically add the project root to Python's search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.model import create_model # type: ignore
from src.utils import load_data # type: ignore
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_and_evaluate(data_path):
    # Load the dataset
    X, y = load_data(data_path)
    X_train, X_test, y_train, y_test = (
        train_test_split(X, y, test_size=0.2, random_state=42)
    )

    # Train the model
    model = create_model()
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Accuracy: {accuracy:.2f}")

    return model, accuracy


if __name__ == "__main__":
    train_and_evaluate("data/iris.csv")
