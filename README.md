```
Практика  –  1
```

# Практика

Для выполнения заданий необходимо: 

1. Создать аккаунт на одном из общедоступных сервисов git (github, gitlab, bitbucket)
2. Создать общедоступный репозиторий. Для работы можно использовать https://product-
downloads.atlassian.com/software/sourcetree/windows/ga/SourceTreeSetup-3.4.15.exe
3. Содержание заданий описано в приложенном документе (доступен для скачивания)
4. В строку ответа на это задание приложите ссылку на ваш проект
5. Для работы с Python рекомендуется установить версию 3.10 или выше python с использованием
venv
6. IDE для разработки скачать от сюда https://www.jetbrains.com/pycharm/download/download-
thanks.html?platform=windows&code=PCC
5. Для установки библиотек используйте pip. **ВАЖНО** их добавление должно идти через файл
requirements, который должен находится в корне проекта

**Общие критерии оценки задач:**

1. Работоспособный код
2. Чистота кода
3.  Плюсом будет использование docstring`ов и аннотаций типов

# Работа с pandas и csv

```
Напишите функцию, которая принимает на вход CSV файл с данными о сотрудниках компании.
В файле должны быть следующие колонки: "Имя", "Возраст", "Должность".
Функция должна вернуть словарь, в котором ключами являются уникальные должности, а
значениями — средний возраст сотрудников на каждой должности.
```
```
Для чтения и работы с csv файлами, нужно использовать библиотеку pandas.
```
```
Пример CSV файла (employees.csv):
```
```
Имя,Возраст,Должность
Алексей,25,Разработчик
Мария,30,Менеджер
Иван,28,Разработчик
Анна,35,Менеджер
```
```
Напишите FastAPI приложение, которое предоставляет API для работы с функцией из задачи 1.1.
Ваше API должно иметь единственный endpoint (POST) "/average_age_by_position", который
принимает файл csv.
В ответе ожидается JSON с результатами работы функции average_age_by_position.
```

```
Работа с pandas и csv  –  2
```
```
Пример ответа
```
```
{
"Разработчик": 26.5,
"Менеджер": 32.
}
```
```
Также добавьте исключения, если файл приходит не валидный, например, неправильный
формат файла, столбцы отличаются и т.д.
В таких случаях ожидается строка с ошибкой и status code 400.
```
Тест кейсы:

```
Input Output
```
```
Имя,Возраст,Должность
Алексей,25,Разработчик
Мария,30,Менеджер
Иван,28,Разработчик
Анна,35,Менеджер
```
```
status code 200
{
"Разработчик": 26.5,
"Менеджер": 32.
}
```
```
Имена,Возраст,Далжность
Алексей,25,Разработчик
Мария,30,Менеджер
Иван,28,Разработчик
Анна,35,Менеджер
```
```
status code 400
Невалидный файл
```
```
Имя,Возраст,Далжность
Алексей,25,Разработчик
Мария,30,Менеджер
Иван,28,Разработчик
Анна,,Менеджер
```
```
status code 200
{
"Разработчик": 26.5,
"Менеджер": 30
}
```
```
Имя,Возраст,Должность
Алексей,,Разработчик
Мария,30,Менеджер
Иван,,Разработчик
Анна,,Менеджер
Михаил,26,Аналитик
Сергей,42,Аналитик
```
```
status code 200
{
"Разработчик": null,
"Менеджер": 30,
"Аналитик": 34,
}
```

```
Фильтрация массива с учетом регистра строки  –  3
```
## 1.

## 2.

# Фильтрация массива с учетом регистра строки

```
Реализуйте функцию соответствующую следующему описанию:
На вход подаётся массив слов зависимых от регистра, для которых необходимо произвести
фильтрацию на основании дублей слов, если в списке найден дубль по регистру, то все
подобные слова вне зависимости от регистра исключаются.
На выходе должны получить уникальный список слов в нижнем регистре.
```
```
Пример
```
```
def find_in_different_registers(words: list[str]):
pass
```
```
words = ['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'Мама', 'ДЯдя', 'брАт',
'Дядя', 'Дядя', 'Дядя']
# find_in_different_registers(words) -> ['папа','брат']
```
```
Дополните ваше приложение на FastAPI новым endpoint (POST) "/find_in_different_registers" для
использования получившейся функции.
На выходе ожидается json с массивом строк.
```
```
Тест кейсы:
```
```
Input Output
```
```
['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'Мама',
'ДЯдя', 'брАт', 'Дядя', 'Дядя', 'Дядя']
```
```
['папа','брат']
```
```
['МАМА', 'Мама', 'БРАТ', 'папа', 'ПАПА', 'ДЯдя', 'брАт',
'Дядя', 'Дядя', 'Дядя']
```
```
['мама', 'брат', 'папа']
```
# Реализация API для хранения и управления данными

```
Напишите API для работы с "to-do" списком. Реализуйте следующие операции: добавление
задач(PUT) "/tasks", удаление задачи(DELETE) "/tasks/<task_id>" , получение списка задач(GET) "/
tasks" , обновление (POST) "/tasks/<task_id>".
Необходимо использовать pydantic для валидации входных данных. Для хранения и манипуляции
данных можно использовать память приложения/sqlite/PostgreSQL/файл на стороне приложения и
т.д.
```
```
Пример списка с задачами
```
```
[{'task': 'Дописать код для упражнения 1.2', 'status': True},
{'task': 'сходить покушать', 'status': False}]
```

```
Реализация API для хранения и управления данными  –  4
```
```
Тест кейсы добавление задачи:
```
**Input Output**

 [{'task': 'Дописать код для упражнения
1.2','status': False},
{'task': 'сходить покушать', 'status': False}]

```
status code 200
[{'task': 'Дописать код для упражнения 1.2','status':
False, task_id: 1},
{'task': 'сходить покушать', 'status': False, 'task_id':
2}]
```
 [{'task': 'Принять таблетки','status': False}] status code 200
[{'task': 'Принять таблетки','status': False, 'task_id':
3}]

[{'status': False}] status code 422

 [{'task': 'Принять таблетки','status': 'неудачно'}] status code 422

```
Тест кейсы удаление задачи:
```
**Input Output**

task_id: 1 status code 200

task_id: 5 status code 404

```
task not found
```
task_id: "пять" status code 424

```
Тест кейсы обновления задачи:
```
**Input Output**

 task_id: 1
{'task': 'Дописать код для упражнения
1.3','status': True}

```
status code 200
{'task': 'Дописать код для упражнения 1.3','status':
True, "task_id": 1}
```
 task_id: 5
{'task': 'Дописать код для упражнения
1.3','status': True}

```
status code 404
task not found
```

```
Работа с PostgreSQL и SQLAlchemy  –  5
```
## 1.

```
Input Output
```
```
 task_id: 1
{'task': 'Дописать код для упражнения
1.3','status': "Выполнено"}
```
```
status code 424
```
```
Тест кейсы получения задачи:
```
```
Input Output
```
```
 task_id: 1 status code 200
{'task': 'Дописать код для упражнения 1.3','status':
True, "task_id": 1}
```
```
task_id: 5 status code 404
task not found
```
# Работа с PostgreSQL и SQLAlchemy

```
Усовершенствуйте решение предыдущей задачи.
Используйте PostgreSQL для хранения данных и sqlalchemy для работы с PostgreSQL.
```
# Тестирование

```
Напишите unit-тесты для вашего приложения с покрытием более 70%. Для написания используйте
библиотеки pytest.
Для запуска тестов используйте команду `pytest`. Все тесты должны лежать в папке tests в корне
приложения.
```
# Контейнеризация приложения

```
Напишите dockerfile и контейнеризируйте ваше приложение.
После сборки и запуска приложение должно быть доступно по 8000 порту.
```
```
Подсказка:
Используйте для сборки образ python:3.10-buster.
```
# Цепное суммирование

```
Реализуйте цепную функцию суммирования.
```

```
Конвертер из integer в Римские цифры  –  6
```
## 2.

## 1.

## 2.

## 3.

## 1.

## 2.

```
Примеры
```
```
chain_sum( 5 )() - > 5
chain_sum( 5 )( 2 )() - > 7
chain_sum( 5 )( 100 )( - 10 )() - > 95
```
```
Напишите unit-тесты для получившейся функции
```
# Конвертер из integer в Римские цифры

```
Реализуйте конвертер из integer в Римские цифры.
Символ Значение
I   
V  5
X 10
L  50
C   
D   
M  1000
```
```
Примеры
```
```
def int_to_roman(num: int):
pass
```
```
int_to_roman( 32 ) - > "XXXII" # XXX = 30, II = 2.
int_to_roman( 54 ) - > "LIV" # L = 50, IV = 4.
int_to_roman( 1984 ) - > "MCMLXXXIV" # M = 1000, CM = 900, LXXX = 80 and IV = 4.
```
```
Подсказка:
Советую сразу учитывать значения с вычитанием (IV, IX, XL и т.д.)
```
```
Дополните ваше приложение новым endpoint (POST) "/int_to_roman" с использованием
получившейся функции.
```
```
Напишите unit-тесты для получившейся функции
```
# API для хранения файлов

```
API для хранения файлов.
Написать API для добавления(POST) "/upload_file" и скачивания (GET) "/download_file/<file_id>"
файлов.
В ответ на удачную загрузку файла должен приходить id для скачивания.
```
```
Добавить архивирование к post запросу, то есть файл должен сжиматься и сохраняться в ZIP
формате.
```

```
Генерация файлов в форматах CSV, JSON и YAML  –  7
```
## 1.

```
a.
b.
2.
a.
b.
3.
4.
```
Критерии проверки:

```
После удачной загрузки файла получен file_id, файл сохранен на стороне сервера.
Без архивации;
С архивацией файл сохраняется в zip.
При выполнении GET запроса с существующим file_id файл удачно скачивается
Если был загружен без архивации приходит в том же формате и размере;
Если был загружен с использованием архивации приходит в формате zip.
Если file_id не найден при GET запросе 404 ответ
Если при загрузке не был передан файл ожидается 424 ответ
```
# Генерация файлов в форматах CSV, JSON и YAML

```
Дан класс DataGenerator, который имеет два метода: generate() -> None, to_file(self, path: str, writer:
BaseWriter) -> None
Метод generate генерирует mock данные формата list[list[int, str, float]] и записывает результат в
переменную класса data
Метод to_file сохраняет значение переменной generated_data в по пути path c помощью метода
write, классов JSONWritter, CSVWritter, YAMLWritter.
Примечание: Если data is None, то пользователь при вызове метода to_file должен получать
предупреждения о том, что данные не были сгенерированы
Допишите реализацию метода Mock.generate, JSONWritter, CSVWritter и YAMLWritter
```
```
from abc import ABC, abstractmethod
from io import StringIO
```
```
class BaseWriter(ABC):
"""
Абстрактный класс с методом write для генерации файла
"""
```
```
@abstractmethod
def write(self, data: list[list[int, str, float]]) - > StringIO:
"""
Записывает данные в строковый объект файла StringIO
```
```
:param data: полученные данные
:return: Объект StringIO с данными из data
"""
pass
```
```
class JSONWriter:
"""Потомок BaseWriter с переопределением метода write для генерации файла в json
формате"""
"""Ваша реализация"""
pass
```

```
Логирование в FastAPI с использованием middleware  –  8
```
```
class CSVWriter:
"""Потомок BaseWriter с переопределением метода write для генерации файла в csv
формате"""
"""Ваша реализация"""
pass
```
```
class YAMLWriter:
"""Потомок BaseWriter с переопределением метода write для генерации файла в yaml
формате"""
"""Ваша реализация"""
pass
```
```
class DataGenerator:
def __init__(self, data: list[list[int, str, float]] = None):
self.data: list[list[int, str, float]] = data
```
```
def generate(self) - > None:
"""
Генерирует матрицу данных размера 4x
"""
data: list[list[int, str, float]] = []
"""Ваша реализация"""
self.data = data
```
```
def to_file(self, path: str, writer: BaseWriter) - > None:
"""
Метод для записи в файл данных полученных после генерации.
Если данных нет, то вызывается кастомный Exception.
:param path: Путь куда требуется сохранить файл
:param writer: Одна из реализаций классов потомков от BaseWriter
"""
```
```
"""Ваша реализация"""
pass
```
# Логирование в FastAPI с использованием middleware

```
Настройте логирование вашего приложения FastAPI.
Реализуйте ваше решение с использованием прослоек(middleware) для каждого вызова API. 
```
```
Формат логов
```
```
[CURRENT_DATETIME] {file: line} LOG_LEVEL - | EXECUTION_TIME_SEC | HTTP_METHOD | URL
| STATUS_CODE |
```
```
[ 2023 - 12 - 15 00 : 00 : 00 ] {example: 62 } INFO | 12 | GET | http: // localhost / example | 200 |
```

```
Реализация UI приложения  –  9
```
```
a.
b.
```
## 1.

```
a.
b.
c.
```
## 2.

```
a.
```
```
Критерии выполнения:
Нет стандартных логов uvicorn
Каждый endpoint имеет лог в формате из задания
```
# Реализация UI приложения

```
Реализуйте простой web ui для конвертера арабских чисел в римские. 
Используйте для этого шаблоны jinja
```
```
На странице размещены 2 x <textarea> и 1 x <button>, это минимальный набор, вы также можете
улучшить страницу по своему желанию. 
Реализовать следующий сценарий:
В 1 ю textarea пользователь записывает число.
Нажимает на кнопку <Конвертировать>.
Во 2 й textarea должен появится результат выполнения, присланный с /int_to_roman, вашего
приложения.
```
```
Реализуйте простой web ui для страницы "Список дел". 
Используйте для этого шаблоны jinja
Минимальный интерфейс представлен на изображении ниже.
```
```
Реализовать следующий сценарий:
Пользователь нажимает на кнопку "добавить дело", перед ним всплывает модальное окно
или c помощью вызывается функция prompt.
```

```
Реализация UI приложения  –  10
```
b.

```
c.
```
d.

```
Пользователь вводит текст нового дела и подтверждает ввод. После подтверждения
должен отправится запрос на добавления в раннее реализованный api, 
при удачном добавлении, при удачном выполнении необходимо обновить список дел,
иначе сообщить пользователю о проблеме.
Пользователь нажимает на чек-бокс созданного дела, дело должно пометится как
выполненное (текст зачеркнут, чек-бокс в состоянии true).
Пользователь нажимает на кнопку удаления (красный крестик), перед ним всплывает
модальное окно
или вызывается функция confirm с предупреждением об удалении, после подтверждения
от пользователя, 
отправляется запрос к api на удаление, при успешном удалении необходимо обновить
список дел, иначе сообщить пользователю о проблеме.
```
