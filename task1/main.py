from fastapi import FastAPI, HTTPException, Query
from typing import Dict
from task1 import average_age_by_position
from urllib.parse import unquote
import json
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/aaaa")
async def root():
    return {"blayt": "i dont get it"}

@app.get("/average_age_by_position/{path_to_file:path}")
async def calculate_average_age(path_to_file:str) -> Dict[str, float]:
    try:
        result = average_age_by_position(path_to_file)
        
        return result

    except Exception as e:
        raise HTTPException(status_code=400, detail='Невалидный файл')
