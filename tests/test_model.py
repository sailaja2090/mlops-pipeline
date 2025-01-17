from src.model import create_model


def test_create_model():
    model = create_model()
    assert model is not None, "Model should not be None"
    assert hasattr(model, "fit"), "Model should have a 'fit' method"
