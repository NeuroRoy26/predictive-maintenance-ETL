import sqlite3 
import logging
import pandas as pd

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

def get_high_risk_units(threshold=50, db_name="factory_data.db"):
    """
    Example of an optimized SQL query to identify machinery at risk.
    Addresses the 'identify and address complex data issues' requirement.
    """
    conn = sqlite3.connect(db_name)
    query = f"""
        SELECT unit_id, MAX(cycle) as total_cycles
        FROM sensor_readings
        WHERE s11 > {threshold}  -- Assuming s11 is a critical temperature sensor
        GROUP BY unit_id
        HAVING total_cycles > 100
        ORDER BY total_cycles DESC;
    """
    report = pd.read_sql(query, conn)
    conn.close()
    return report

def create_analytical_views(db_name="factory_data.db"):
    """
    Creates a 'Gold Level' table for high-level manufacturing reporting.
    This simulates 'Documenting Dashboards' as requested in the JD.
    """
    conn = sqlite3.connect(db_name)
    # This SQL query calculates the Remaining Useful Life (RUL) trend
    query = """
    CREATE VIEW IF NOT EXISTS v_machine_health_alerts AS
    SELECT 
        unit_id, 
        MAX(cycle) as total_runtime,
        AVG(s11) as avg_temp, 
        AVG(s12) as avg_pressure,
        CASE 
            WHEN MAX(cycle) > 150 THEN 'CRITICAL'
            WHEN MAX(cycle) > 100 THEN 'WARNING'
            ELSE 'HEALTHY'
        END as health_status
    FROM sensor_readings
    GROUP BY unit_id;
    """
    conn.execute(query)
    conn.close()