import pandas as pd
from typing import Dict

def check_columns(workers_table:pd.DataFrame) -> bool:
    '''
    проверка на колонки: "Имя", "Возраст", "Должность".
    '''
    required_cols = workers_table.columns 
    return (('Имя' in required_cols) and ('Возраст' in required_cols) and ('Должность' in required_cols))
    
def average_age_by_position(s:str='path_to_csv_file.csv') -> Dict[str, float]:
    '''
    вход: file.csv с колонками "Имя", "Возраст", "Должность"
    выход: словарь вида: d["Должность"] == средний_возраст_по_должности
    '''
    workers_table = pd.read_csv(s)
    
    if  not check_columns(workers_table):
        raise ValueError(f'Файл {s} не содержит нужные столбцы: Имя, Возраст, Должность')
    

    avg_age_position = {}
    grouped_data = workers_table.groupby('Должность')['Возраст'].mean().reset_index()

    for _, row in grouped_data.iterrows():
        position = row['Должность']
        avg_age_position[position] = row['Возраст']
    print(avg_age_position)
    return avg_age_position
