import logging
from ingest import load_raw_data
from transform import clean_sensor_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline():
    input_file = 'data/CMaps/train_FD001.txt' 
    
    logging.info("Starting Predictive Maintenance ETL Pipeline...")

    raw_df = load_raw_data(input_file)
    
    if raw_df is not None:
        processed_df = clean_sensor_data(raw_df)
        
        if not processed_df.empty:
            logging.info(f"Pipeline Complete. Processed {processed_df.shape[0]} valid records.")
            
            output_path = 'data/processed_sensor_data.csv'
            processed_df.to_csv(output_path, index=False)
            logging.info(f"Cleaned data saved to {output_path}")
        else:
            logging.warning("Transformation resulted in an empty dataset. Check sensor variance.")
    else:
        logging.error("Pipeline failed during the ingestion stage.")

if __name__ == "__main__":
    run_pipeline()