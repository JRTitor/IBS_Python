import requests

url = 'http://127.0.0.1:8000/find_in_different_registers'
data = {"words": ['МАМА', 'Мама', 'БРАТ', 'папа', 'ПАПА', 'ДЯдя', 'брАт', 'Дядя', 'Дядя', 'Дядя']}
response = requests.post(url, json=data)

print(response.json())
