import sys
import os

# Add the root project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.model import create_model


def test_create_model():
    model = create_model()
    assert model is not None, "Model should not be None"
    assert hasattr(model, "fit"), "Model should have a 'fit' method"
