import os
import sys
from decimal import Decimal

# Ensure the runtime environment can resolve the root module source directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.transform import process_transaction

def test_process_transaction_precision():
    """Verify precision decimal calculations work flawlessly."""
    sample_record = {
        "signal_id": "SIG-TEST",
        "Entry Price": "100.00",
        "Quantity": "10"
    }
    result = process_transaction(sample_record)
    assert isinstance(result, Decimal)
    assert result == Decimal('1000.00')
