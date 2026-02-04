import pandas as pd
import numpy as np

def clean_sensor_data(df):
    """
    Cleans raw industrial sensor data by removing low-variance features
    and smoothing noise.
    """
    unique_counts = df.nunique()
    constant_cols = unique_counts[unique_counts <= 1].index
    df_cleaned = df.drop(columns=constant_cols)
    
    df_cleaned = df_cleaned.clip(lower=df_cleaned.quantile(0.01), 
                                 upper=df_cleaned.quantile(0.99), axis=1)
    
    sensor_cols = [col for col in df_cleaned.columns if 'sensor' in col.lower()]
    df_cleaned[sensor_cols] = df_cleaned[sensor_cols].rolling(window=5).mean()
    
    return df_cleaned.dropna()