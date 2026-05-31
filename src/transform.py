import os
from decimal import Decimal
from typing import Dict, Any

def process_transaction(record: Dict[str, Any]) -> Decimal:
    """
    Transforms raw incoming transactional data and extracts calculated values
    utilizing strict high-precision Decimal formatting.
    """
    # Extract entries cleanly, defaulting to '0' if keys are missing
    entry_price_str = record.get("Entry Price", "0")
    quantity_str = record.get("Quantity", "0")
    
    # Convert parameters strictly into Decimal to mitigate standard float truncation issues
    price = Decimal(str(entry_price_str))
    quantity = Decimal(str(quantity_str))
    
    # Compute base capital value requirements
    capital_needed = price * quantity
    
    return capital_needed
