from decimal import Decimal, InvalidOperation
from typing import Dict, Any

DEFAULT_PRECISION = "0.01"
MAX_QUANTITY_LIMIT = Decimal("1000000")
MAX_PRICE_LIMIT = Decimal("5000000")


def validate_signal_payload(record: Dict[str, Any]) -> bool:
    """
    Validates structural presence, non-numeric strings, negative ranges,
    and outlier boundaries before committing data to execution.
    """
    required_keys = ["Entry Price", "Quantity"]
    if not all(key in record for key in required_keys):
        return False

    try:
        # Intercept non-numeric parsing anomalies like "INVALID" or None elements
        raw_price = record["Entry Price"]
        raw_qty = record["Quantity"]

        if raw_price is None or raw_qty is None:
            return False

        price = Decimal(str(raw_price))
        qty = Decimal(str(raw_qty))

        # Value-range protection guards (reject negative bounds or absolute zero volume)
        if price <= 0 or qty <= 0:
            return False

        # Extreme integer scalability limit safeguards
        if qty > MAX_QUANTITY_LIMIT or price > MAX_PRICE_LIMIT:
            return False

        return True

    except (ValueError, TypeError, InvalidOperation, ArithmeticError):
        # Gracefully handle validation failure without crashing the runner engine
        return False
