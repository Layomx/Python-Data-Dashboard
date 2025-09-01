import logging
from pathlib import Path

# Logging configuration
logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def setup_logging():
    """
    Sets up the logging configuration for the application.
    """
    logger.info("Logging is set up.")
    
def debug_dataframe(df, name = "DataFrame"):
    """
    Logs the shape and first few rows of a DataFrame for debugging purposes.

    Args:
        df (pd.DataFrame): The DataFrame to be inspected.
        name (str, optional): Name to identify the DataFrame in logs. Defaults to "DataFrame".
    """
    logger.info(f"{name}: {df.shape[0]} filas, {df.shape[1]} columns")
    logger.info(f"Columns: {list(df.columns)}")
    if not df.empty:
        logger.info(f"Data examples:\n{df.head(5).to_string()}")