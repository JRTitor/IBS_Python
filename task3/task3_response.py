import requests

# добавить задачу
response = requests.put("http://127.0.0.1:8000/tasks", json={"task": "Новая задача", "status": False})
print(response.json()) 

# получить список задач
response = requests.get("http://127.0.0.1:8000/tasks")
print(response.json())

# Обновить задачи по task_id (например, task_id=1)
response = requests.post("http://127.0.0.1:8000/tasks/1", json={"task": "Обновленная задача", "status": True})
print(response.json()) 

response = requests.post("http://127.0.0.1:8000/tasks/1", json={"task": "Обновленная задача", "status": "Выполнено"})
print(response.status_code) 

# Удалеить задачи по task_id (например, task_id=1)
response = requests.delete("http://127.0.0.1:8000/tasks/1")
print(response.status_code)

response = requests.delete("http://127.0.0.1:8000/tasks/1")
print(response.status_code)


