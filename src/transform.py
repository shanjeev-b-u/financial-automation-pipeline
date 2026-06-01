import os
import sys
import logging
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Any, Optional

# Enforce explicit root module visibility for runner environments
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.config import validate_signal_payload, DEFAULT_PRECISION

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("DataPipeline")

def process_transaction(record: Dict[str, Any]) -> Optional[Decimal]:
    """Transforms transaction logs and calculates capital requirements securely."""
    signal_id = record.get("signal_id", "UNKNOWN-SIGNAL")
    logger.info(f"Processing execution signal: {signal_id}")

    if not validate_signal_payload(record):
        logger.error(f"Transaction validation failed for {signal_id}")
        return None

    try:
        price = Decimal(str(record["Entry Price"]))
        quantity = Decimal(str(record["Quantity"]))
        
        capital_needed = price * quantity
        quantized_result = capital_needed.quantize(Decimal(DEFAULT_PRECISION), rounding=ROUND_HALF_UP)
        
        logger.info(f"Signal {signal_id} parsed successfully: {quantized_result}")
        return quantized_result

    except Exception as e:
        logger.critical(f"Math calculation exception on signal {signal_id}: {str(e)}")
        return None

if __name__ == "__main__":
    mock_record = {
        "signal_id": "SIG-LOCAL-RUN",
        "Entry Price": "150.75",
        "Quantity": "25"
    }
    process_transaction(mock_record)
