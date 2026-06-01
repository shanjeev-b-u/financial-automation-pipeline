import os
import sys
from decimal import Decimal

# Ensure the runtime environment can resolve the root module source directory smoothly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.transform import process_transaction  # noqa: E402
from src.pipeline_runner import simulate_llm_noise_filter, javascript_style_risk_processor  # noqa: E402


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


def test_simulate_llm_noise_filter():
    """Verify that the AI filter layer drops noisy signals below confidence limits."""
    high_noise = {"signal_id": "SIG-NOISE", "Confidence Score": "0.34"}
    clean_signal = {"signal_id": "SIG-CLEAN", "Confidence Score": "0.95"}
    
    assert simulate_llm_noise_filter(high_noise) is False
    assert simulate_llm_noise_filter(clean_signal) is True


def test_javascript_style_risk_processor():
    """Verify that extreme corporate capital exposures trigger internal blocks."""
    extreme_trade = javascript_style_risk_processor(25000.00, 5.0)  # $125,000 exposure
    safe_trade = javascript_style_risk_processor(100.00, 10.0)      # $1,000 exposure
    
    assert extreme_trade is False
    assert safe_trade is True
