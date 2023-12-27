import pytest
import pandas as pd
from task1 import average_age_by_position, check_columns

def test_columns_position():
    workers_table = pd.DataFrame({'Имя': ['John', 'Jane'], 'Возраст': [25, 28], 'Должность': ['Programmer', 'Designer']})
    assert check_columns(workers_table) is True

    workers_table = pd.DataFrame({'Имя': ['John', 'Jane'], 'Возраст': [25, 28], 'Дfлжность': ['Programmer', 'Designer']})
    assert check_columns(workers_table) is False

def test_average_age_by_position():
    workers_table = pd.DataFrame({'Имя': ['John', 'Jane'], 'Возраст': [25, 28], 'Должность': ['Programmer', 'Designer']})
    result = average_age_by_position(workers_table_in=workers_table)
    assert result == {'Programmer': 25.0, 'Designer': 28.0}

    workers_table = pd.DataFrame({'Имя': ['John', 'Jane'], 'Возраст': [25, 28], 'Должность': ['Programmer', 'Designer']})
    result = average_age_by_position(workers_table_in=workers_table)
    assert result != {'Programmer': 250.0, 'Designer': 28.0}

