from fastapi import FastAPI, HTTPException, File, UploadFile
from typing import List, Dict
from task1.task1 import average_age_by_position
from task2.task2 import find_in_different_registers
import json
from pydantic import BaseModel

class Words(BaseModel):
    words: List[str]

app = FastAPI()


@app.post("/average_age_by_position/")
async def calculate_average_age(file: UploadFile = File(...)) :
    try:
        contents = await file.read() ## читаем файл и заносим в contents
        result = average_age_by_position(contents)

        return json.dumps(result, indent=4, ensure_ascii=False) ##  возвращаем json без аски символов, иначе мы не увидим русских букв

    except Exception as e:
        raise HTTPException(status_code=400, detail='Невалидный файл')
    
@app.post("/find_in_different_registers", response_model=List[str])
async def find_unique_words(words: Words):
    try:
        input_words = words.words
        print(input_words)
        unique_words = find_in_different_registers(input_words)
        return unique_words
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))