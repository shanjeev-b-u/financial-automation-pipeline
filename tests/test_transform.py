import pytest
from src.transform import calculate_trade_risk

def test_calculate_trade_risk_precision():
    """Validates that financial logic avoids binary float truncation and rounds perfectly."""
    sample_signal = {
        "Entry Price": "100.05",
        "Quantity": "10"
    }
    
    result = calculate_trade_risk(sample_signal)
    
    # Expected exact calculations based on 3% risk rules:
    # stop_loss = 100.05 * 0.97 = 97.0485 -> Rounded half up: 97.05
    # risk_per_share = 100.05 - 97.05 = 3.00
    # target = 100.05 + (3.00 * 2) = 106.05
    # capital_needed = 100.05 * 10 = 1000.50 -> Rounded half up: 1001
    
    assert result["stop_loss"] == 97.05
    assert result["target"] == 106.05
    assert result["capital_needed"] == 1001

def test_calculate_trade_risk_missing_data():
    """Ensures fallback values behave predictably without throwing unhandled exceptions."""
    malformed_signal = {}
    result = calculate_trade_risk(malformed_signal)
    
    assert result["stop_loss"] == 0.0
    assert result["target"] == 0.0
    assert result["capital_needed"] == 0
