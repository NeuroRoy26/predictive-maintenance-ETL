import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_raw_data(file_path):
    """
    Simulates data ingestion from a factory sensor hub.
    Includes error handling for missing or corrupt files.
    """
    if not os.path.exists(file_path):
        logging.error(f"Data source not found at {file_path}")
        raise FileNotFoundError(f"Missing industrial data file.")

    try:
        column_names = ['unit_id', 'cycle', 'setting1', 'setting2', 'setting3'] + \
                       [f's{i}' for i in range(1, 22)]
        
        df = pd.read_csv(file_path, sep='\s+', header=None, names=column_names)
        logging.info(f"Successfully ingested {len(df)} rows from {file_path}")
        return df
    except Exception as e:
        logging.critical(f"Failed to ingest data: {e}")
        return None