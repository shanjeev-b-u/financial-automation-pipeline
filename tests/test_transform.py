import os
import sys
from decimal import Decimal

# Ensure the runtime environment can resolve the root module source directory smoothly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.transform import process_transaction  # noqa: E402


def test_process_transaction_precision():
    """Verify high-precision decimal calculation checks function flawlessly."""
    sample = {"signal_id": "SIG-01", "Entry Price": "100.05", "Quantity": "10"}
    assert process_transaction(sample) == Decimal('1000.50')


def test_process_transaction_invalid_boundaries():
    """Verify that negative bounds and corrupt strings return None instead of crashing."""
    negative_price = {"signal_id": "SIG-ERR-01", "Entry Price": "-50.00", "Quantity": "10"}
    invalid_string = {"signal_id": "SIG-ERR-02", "Entry Price": "INVALID", "Quantity": "10"}
    none_payload = {"signal_id": "SIG-ERR-03", "Entry Price": None, "Quantity": "5"}
    missing_data = {"signal_id": "SIG-ERR-04"}

    assert process_transaction(negative_price) is None
    assert process_transaction(invalid_string) is None
    assert process_transaction(none_payload) is None
    assert process_transaction(missing_data) is None


def test_process_transaction_extreme_limits():
    """Verify extreme integer protection limits flag outlier data anomalies safely."""
    outlier_signal = {"signal_id": "SIG-LIMIT", "Entry Price": "9999999999", "Quantity": "5"}
    assert process_transaction(outlier_signal) is None
