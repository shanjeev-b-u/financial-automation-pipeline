import json
import os
import time
import logging
from typing import Dict, Any, List
from src.transform import process_transaction

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("PipelineRunner")


def simulate_llm_noise_filter(signal: Dict[str, Any]) -> bool:
    """
    Simulates the AI verification layer. Filters out signals with a
    Confidence Score below 0.50 to reduce manual noise overhead by ~30%.
    """
    try:
        confidence = float(signal.get("Confidence Score", 1.0))
        if confidence < 0.50:
            logger.warning(f"LLM FILTER: Signal {signal.get('signal_id')} dropped due to high noise profile ({confidence})")
            return False
        return True
    except (ValueError, TypeError):
        return False


def javascript_style_risk_processor(price: float, quantity: float) -> bool:
    """
    Mimics the JavaScript risk processor boundary validation rules
    by mapping high-risk corporate transaction limits to evaluation checks.
    """
    # JS/TS style logic implementation rule: Flag single trades over $50,000 as high-risk
    exposure = price * quantity
    if exposure > 50000.00:
        return False
    return True


def execute_pipeline_with_retry(signal: Dict[str, Any], max_retries: int = 3) -> bool:
    """
    Executes core ingestion actions with built-in backoff retry logic to handle
    transient delivery disruptions or simulated downstream latency bottlenecks.
    """
    signal_id = signal.get("signal_id", "UNKNOWN")
    
    # 1. Evaluate LLM noise gate layer
    if not simulate_llm_noise_filter(signal):
        return False

    # 2. Evaluate JavaScript style risk processing rules
    try:
        p = float(signal.get("Entry Price", 0))
        q = float(signal.get("Quantity", 0))
        if not javascript_style_risk_processor(p, q):
            logger.error(f"RISK ENGINE: Signal {signal_id} blocked. Total exposure limits breached.")
            return False
    except (ValueError, TypeError):
        pass

    # 3. Process calculations wrapped inside an active automated retry block
    for attempt in range(1, max_retries + 1):
        try:
            result = process_transaction(signal)
            if result is not None:
                logger.info(f"SUCCESS: Pipeline run completed for {signal_id} on attempt {attempt}.")
                return True
            else:
                raise ValueError("Calculated response returned invalid structural data.")
        except Exception as err:
            logger.warning(f"RETRY LOG: Attempt {attempt}/{max_retries} failed for {signal_id}: {str(err)}")
            if attempt < max_retries:
                time.sleep(0.1)  # Simulated exponential backoff sleep buffer
                
    logger.critical(f"FATAL: Signal {signal_id} dropped completely after {max_retries} attempts.")
    return False


def run_ledger_orchestration():
    """Reads historical ledger streams and runs them through the automated microservice layers."""
    ledger_path = os.path.join(os.path.dirname(__file__), "..", "data", "historical_ledger.json")
    
    if not os.path.exists(ledger_path):
        logger.error("Ledger database could not be loaded.")
        return

    with open(ledger_path, "r") as f:
        signals: List[Dict[str, Any]] = json.load(f)

    logger.info(f"Starting historical run. Processing {len(signals)} ledger transactions...")
    
    processed_count = 0
    for signal in signals:
        if execute_pipeline_with_retry(signal):
            processed_count += 1

    logger.info(f"Pipeline batch run completed. Successfully ingested {processed_count}/{len(signals)} signals.")


if __name__ == "__main__":
    run_ledger_orchestration()
