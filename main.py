from fastapi import FastAPI, HTTPException, File, UploadFile
from typing import List, Dict
from task1.task1 import average_age_by_position
from task2.task2 import find_in_different_registers
from task8.task8 import int_to_roman
import json
from pydantic import BaseModel

class Words(BaseModel): # модель для 
    words: List[str]

class InputData(BaseModel):
    number: int

app = FastAPI()


"""
This function takes a file as input and calculates the average age by position of the employees in the file.

Args:
    file (bytes): The contents of the file as a byte string

Returns:
    Dict[str, float]: A dictionary containing the average age by position and the total number of employees

Raises:
    HTTPException: If the file is not valid
"""
@app.post("/average_age_by_position/")
async def calculate_average_age(file: UploadFile = File(...)) :
    try:
        contents = await file.read() ## read the file and store it in contents
        result = average_age_by_position(contents)

        return json.dumps(result, indent=4, ensure_ascii=False) ##  return json without ascii characters, otherwise we won't see russian letters

    except Exception as e:
        raise HTTPException(status_code=400, detail='Invalid file')


"""
This function takes a list of words as input and returns a list of unique words that appear in at least two different registers.

Args:
    words (list): A list of words

Returns:
    list: A list of unique words that appear in at least two different registers

Raises:
    ValueError: If the input is not a list
"""
@app.post("/find_in_different_registers", response_model=List[str])
async def find_unique_words(words: Words):
    try:
        input_words = words.words
        print(input_words)
        unique_words = find_in_different_registers(input_words)
        return unique_words
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


"""
This function takes a number as input and returns the roman numeral representation of the number.

Args:
    data (InputData): A pydantic model containing the input data

Returns:
    Dict[str, str]: A dictionary containing the roman numeral representation of the input number
"""
@app.post("/int_to_roman", response_model=Dict[str, str])
def convert_to_roman(data: InputData):
    result = int_to_roman(data.number)
    return {"roman_number": result}