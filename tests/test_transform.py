import os
import sys
from decimal import Decimal
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.transform import process_transaction

def test_process_transaction_precision():
    """Verify high-precision decimal processing checks function flawlessly."""
    sample = {"signal_id": "SIG-01", "Entry Price": "100.05", "Quantity": "10"}
    assert process_transaction(sample) == Decimal('1000.50')

def test_process_transaction_invalid_boundaries():
    """Verify that negative bounds and corrupt payloads return None instead of crashing."""
    negative_price = {"signal_id": "SIG-ERR-01", "Entry Price": "-50.00", "Quantity": "10"}
    invalid_string = {"signal_id": "SIG-ERR-02", "Entry Price": "FREE", "Quantity": "10"}
    missing_data = {"signal_id": "SIG-ERR-03"}
    
    assert process_transaction(negative_price) is None
    assert process_transaction(invalid_string) is None
    assert process_transaction(missing_data) is None

def test_process_transaction_extreme_limits():
    """Verify extreme integer protection bounds flag outlier values safely."""
    outlier_signal = {"signal_id": "SIG-LIMIT", "Entry Price": "9999999999", "Quantity": "5"}
    assert process_transaction(outlier_signal) is None
