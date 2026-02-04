import logging
from ingest import load_raw_data
from transform import clean_sensor_data
from database import load_to_warehouse

def validate_data(df):
    """Automated Quality Check: Ensures accuracy and completeness."""
    if df.isnull().values.any():
        return False, "Null values detected"
    if len(df) < 100:
        return False, "Data volume too low - possible ingestion error"
    return True, "Valid"

def run_automated_pipeline():
    raw_df = load_raw_data('data/CMaps/train_FD001.txt')
    
    processed_df = clean_sensor_data(raw_df)
    
    is_valid, msg = validate_data(processed_df)
    
    if is_valid:
        load_to_warehouse(processed_df)
    else:
        logging.critical(f"Pipeline Halted: {msg}")

if __name__ == "__main__":
    run_automated_pipeline()