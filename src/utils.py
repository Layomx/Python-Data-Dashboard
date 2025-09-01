import logging
from pathlib import Path
from textwrap import shorten

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
        
    
def format_currency(amount):
    """
    Formats a number as currency, using K for thousands and M for millions.

    Args:
        amount (float or int): The numeric value to format.

    Returns:
        st: The formatted currency string.
    """
    if amount >= 1_000_000:
        return f"${amount/1_000_000:.2f}M"
    elif amount >= 1_000:
        return f"${amount/1_000:.2f}K"
    else:
        return f"${amount:.2f}"

def shorten_text(text, max_length=20):
    """
    Shortens a text string to a specified maximum length, adding ellipsis if necessary.

    Args:
        text (str): The text string to shorten.
        max_length (int, optional): Maximum length of the output string. Defaults to 20.

    Returns:
        str: The shortened text string.
    """
    return shorten(text, width=max_length, placeholder="...")