import os
import zipfile

from fastapi import FastAPI, File, HTTPException

app = FastAPI()

# Хранилище файлов
files = {}


@app.post("/upload_file")
async def upload_file(file: File):
    # Проверяем, что был передан файл
    if file is None:
        raise HTTPException(status_code=424, detail="Файл не передан")

    # Сжимаем файл, если включена архивация
    file_path = file.filename
    if file_path.endswith(".zip"):
        file_bytes = file.read()
    else:
        file_bytes = zipfile.compress(file.read())

    # Генерируем ID файла
    file_id = os.urandom(16).hex()

    # Сохраняем файл
    files[file_id] = file_bytes

    return {"file_id": file_id}


@app.get("/download_file/{file_id}")
async def download_file(file_id: str):
    # Проверяем, что файл существует
    if file_id not in files:
        raise HTTPException(status_code=404, detail="Файл не найден")

    # Получаем файл
    file_bytes = files[file_id]

    # Распаковываем файл, если он был заархивирован
    if file_bytes.startswith(b"PK"):
        file_bytes = zipfile.decompress(file_bytes)

    return file_bytes


