import pandas as pd
import numpy as np

def clean_sensor_data(df):
    """
    Cleans raw industrial sensor data by removing low-variance features
    and smoothing noise.
    """
    # 1. Identify and drop constant columns (Sensors that aren't moving)
    unique_counts = df.nunique()
    constant_cols = unique_counts[unique_counts <= 1].index
    df_cleaned = df.drop(columns=constant_cols)
    
    # 2. Handle outliers using a simple clip (Factory sensors often have 'spike' errors)
    # We use the 1st and 99th percentile
    df_cleaned = df_cleaned.clip(lower=df_cleaned.quantile(0.01), 
                                 upper=df_cleaned.quantile(0.99), axis=1)
    
    # 3. Smoothing: 5-cycle rolling average to simulate 'real-time' trend analysis
    # Tesla values 'monitoring and troubleshooting'
    sensor_cols = [col for col in df_cleaned.columns if 'sensor' in col.lower()]
    df_cleaned[sensor_cols] = df_cleaned[sensor_cols].rolling(window=5).mean()
    
    return df_cleaned.dropna()