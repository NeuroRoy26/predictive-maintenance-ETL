import sqlite3 
import logging

def load_to_warehouse(df, db_name="factory_data.db"):
    """
    Loads the processed sensor data into a SQL database.
    Directly addresses the 'optimize SQL queries' JD requirement.
    """
    try:
        conn = sqlite3.connect(db_name)
        df.to_sql('sensor_readings', conn, if_exists='replace', index=False)
        logging.info(f"Successfully loaded {len(df)} rows to SQL table 'sensor_readings'")
        
        query = "CREATE INDEX IF NOT EXISTS idx_unit_cycle ON sensor_readings (unit_id, cycle)"
        conn.execute(query)
        conn.close()
    except Exception as e:
        logging.error(f"Database Load Error: {e}")