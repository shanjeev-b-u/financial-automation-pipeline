import os
from decimal import Decimal
from typing import Dict, Any

# Global pipeline configurations
DEFAULT_PRECISION = "0.01"
MAX_QUANTITY_LIMIT = Decimal("1000000")
MAX_PRICE_LIMIT = Decimal("5000000")

def validate_signal_payload(record: Dict[str, Any]) -> bool:
    """
    Validates structural presence and raw metrics safety constraints 
    before committing transactional data to decimal conversion pipelines.
    """
    required_keys = ["Entry Price", "Quantity"]
    if not all(key in record for key in required_keys):
        return False
        
    try:
        price = Decimal(str(record["Entry Price"]))
        qty = Decimal(str(record["Quantity"]))
        
        # Enforce baseline technical boundary limits (no negatives, no extreme integers)
        if price <= 0 or qty <= 0:
            return False
        if qty > MAX_QUANTITY_LIMIT or price > MAX_PRICE_LIMIT:
            return False
            
        return True
    except (ValueError, TypeError, ArithmeticError):
        return False
