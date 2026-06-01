import pytest


@pytest.fixture
def base_valid_signal():
    """Provides a baseline valid transactional signal dictionary payload."""
    return {
        "signal_id": "SIG-9982X",
        "Entry Price": "100.05",
        "Quantity": "10",
        "Source": "Telegram Alpha Channel Stream"
    }


@pytest.fixture
def zero_value_signal():
    """Provides a transactional record representing zeroed volume metrics."""
    return {
        "signal_id": "SIG-ZERO",
        "Entry Price": "0.00",
        "Quantity": "0"
    }
