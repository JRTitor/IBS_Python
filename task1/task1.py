import pandas as pd
from typing import Dict
import io

def check_columns(workers_table: pd.DataFrame) -> bool:
    """
    Checks if the given workers table has the required columns: "Имя", "Возраст", "Должность".

    Args:
        workers_table (pd.DataFrame): The workers table to check.

    Returns:
        bool: True if the table has the required columns, False otherwise.
    """
    required_cols = workers_table.columns
    return (('Имя' in required_cols) and ('Возраст' in required_cols) and ('Должность' in required_cols))
    
def average_age_by_position(s:str='path_to_csv_file.csv', workers_table_in:pd.DataFrame=None) -> Dict[str, float]:
    """
    This function calculates the average age of workers by their position.

    Parameters:
    s (str): The path to the CSV file.

    Returns:
    Dict[str, float]: A dictionary where the keys are the positions and the values are the average ages.

    Raises:
    ValueError: If the input file is not valid.
    """
    if workers_table_in is None:
        if isinstance(s, str):
            workers_table = pd.read_csv(s)
        else:
            workers_table = pd.read_csv(io.BytesIO(s))
    else:
        workers_table = workers_table_in
    
    if  not check_columns(workers_table):
        raise ValueError(f'Invalid input file')
    

    avg_age_position = {}
    grouped_data = workers_table.groupby('Должность')['Возраст'].mean().reset_index()

    for _, row in grouped_data.iterrows():
        position = row['Должность']
        avg_age_position[position] = None  if pd.isna(row['Возраст']) else row['Возраст']  # чтобы в json был null a не nan
    return avg_age_position
