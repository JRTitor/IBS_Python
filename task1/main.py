from fastapi import FastAPI, HTTPException, File, UploadFile
from typing import Dict
from task1 import average_age_by_position
import json
app = FastAPI()


@app.post("/average_age_by_position/")
async def calculate_average_age(file: UploadFile = File(...)) :
    try:
        contents = await file.read() ## читаем файл и заносим в contents
        result = average_age_by_position(contents)

        return json.dumps(result, indent=4, ensure_ascii=False) ##  возвращаем json без аски символов, иначе мы не увидим русских букв

    except Exception as e:
        raise HTTPException(status_code=400, detail='Невалидный файл')
