import pandas as pd
from pathlib import Path
from utils import debug_dataframe, logger

def load_data():
    """_summary_

    Returns:
        _type_: _description_
    """
    try:
        df = pd.read_csv(".../data/Superstore.csv", encoding = 'latin1')
        logger.info("Data loaded successfully.")
        debug_dataframe(df, "Superstore Original Data")
        return df
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        return None