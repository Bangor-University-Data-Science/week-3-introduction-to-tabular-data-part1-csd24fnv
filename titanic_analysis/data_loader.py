import pandas as pd

def load_titanic_data(filepath: str) -> pd.DataFrame:
    """
    Loads the Titanic dataset from the specified file path.
    
    Args:
        filepath (str): Path to the Titanic CSV file.
    
    Returns:
        pd.DataFrame: Loaded Titanic dataset as a DataFrame.
    """
    df = pd.read_csv("D:\\DS\\week-3-introduction-to-tabular-data-part1-csd24fnv\\data\\titanic.csv")
    return df
