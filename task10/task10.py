from abc import ABC, abstractmethod
from io import StringIO
from typing import List

class BaseWriter(ABC):
   """
   Абстрактный класс с методом write для генерации файла
   """
   @abstractmethod
   def write(self, data: list[list[int, str, float]]) -> StringIO:
      """
      Записывает данные в строковый объект файла StringIO
      :param data: полученные данные
      :return: Объект StringIO с данными из data
      """
      pass


class JSONWriter(BaseWriter):
   """Потомок BaseWriter с переопределением метода write для генерации файла в json
   формате
   """
   """Ваша реализация"""
   pass


class CSVWriter(BaseWriter):
   """Потомок BaseWriter с переопределением метода write для генерации файла в csv
   формате
   """
   """Ваша реализация"""
   pass


class YAMLWriter(BaseWriter):
   """Потомок BaseWriter с переопределением метода write для генерации файла в yaml
   формате
   """
   """Ваша реализация"""
   pass


class DataGenerator:
   def __init__(self, data: list[list[int, str, float]] = None):
      self.data: list[list[int, str, float]] = data
      
   def generate(self) -> None:
      """
      Генерирует матрицу данных размера 4x4
      """
      data: list[list[int, str, float]] = []
      """Ваша реализация"""
      data = [[i, str(i), float(i)] for i in range(4)]
      self.data = data
        
   def to_file(self, path: str, writer: BaseWriter) -> None:
      """
      Метод для записи в файл данных полученных после генерации.
      Если данных нет, то вызывается кастомный Exception.
        :param path: Путь куда требуется сохранить файл
        :param writer: Одна из реализаций классов потомков от BaseWriter
      """
      """Ваша реализация"""
      if not self.data:
         raise ValueError("Data not generated. Please generate data before saving to file.")
      
      with open(path, "w") as file:
         file.write(writer.write(self.data))
