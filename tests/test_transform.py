import os
import sys
from decimal import Decimal
import pytest

# Ensure the runtime environment can resolve the root module source directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.transform import process_transaction

def test_process_transaction_precision(base_valid_signal):
    """CASE 1: Verify high-precision decimal multiplication works flawlessly."""
    result = process_transaction(base_valid_signal)
    assert isinstance(result, Decimal)
    assert result == Decimal('1000.50')

def test_process_transaction_zero_boundaries(zero_value_signal):
    """CASE 2: Verify the calculator handles absolute zero values without crashing."""
    result = process_transaction(zero_value_signal)
    assert result == Decimal('0.00')

def test_process_transaction_missing_keys():
    """CASE 3: Verify fallback handling and default assumptions when key metrics are missing."""
    empty_payload = {"signal_id": "SIG-EMPTY"}
    result = process_transaction(empty_payload)
    assert result == Decimal('0')

def test_process_transaction_fractional_quantities():
    """CASE 4: Verify decimal precision tracking when dealing with fractional volume limits."""
    fractional_signal = {
        "signal_id": "SIG-FRAC",
        "Entry Price": "50.50",
        "Quantity": "2.5"
    }
    # 50.50 * 2.5 = 126.25
    result = process_transaction(fractional_signal)
    assert result == Decimal('126.25')

def test_process_transaction_extreme_integers():
    """CASE 5: Verify processing robustness against massive enterprise scale values."""
    macro_signal = {
        "signal_id": "SIG-MACRO",
        "Entry Price": "125000.00",
        "Quantity": "10000"
    }
    result = process_transaction(macro_signal)
    assert result == Decimal('1250000000.00')

def test_process_transaction_type_handling():
    """CASE 6: Verify internal parser safely forces conversion out of native integer input types."""
    hybrid_signal = {
        "signal_id": "SIG-HYBRID",
        "Entry Price": 100,  # Passed as pure int rather than string
        "Quantity": 5        # Passed as pure int rather than string
    }
    result = process_transaction(hybrid_signal)
    assert isinstance(result, Decimal)
    assert result == Decimal('500')
