import csv
import os
import re
from tabulate import tabulate
from typing import List


class PriceMachine:
    """Класс загрузки, поиска и отображения данных"""
    headers = ['№', 'Наименование', 'цена', 'вес', 'файл', 'цена за кг.']

    def __init__(self):
        self.data = []

    def load_prices(self, directory: str):
        self.data = []
        for filename in os.listdir(directory):
            if filename.endswith('.csv') and 'price' in filename.lower():
                self._load_file(os.path.join(directory, filename))

    def _load_file(self, filepath: str):
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self._process_row(filepath, row)
        except (IOError, csv.Error) as e:
            print(f"Ошибка при чтении файла {filepath}: {e}")

    def _process_row(self, filename, row: dict):
        try:
            product_name = self._extract_value(row, r'(название|продукт|товар|наименование)')
            price = float(self._extract_value(row, r'(цена|розница)').replace(',', '.'))
            weight = float(self._extract_value(row, r'(фасовка|масса|вес)').replace(',', '.'))
            self.data.append([product_name, price, weight, filename, round(price / weight, 2)])
        except (TypeError, ValueError) as exc:
            print(f"Ошибка при обработке строки {row}: {exc}")

    def _extract_value(self, row: dict, pattern: str):
        for column_name, value in row.items():
            if re.search(pattern, column_name, re.IGNORECASE):
                return value.strip()
        return ""

    def search_items(self, query: str):
        results = [row for row in self.data if re.search(query, row[0], re.IGNORECASE)]
        return sorted(results, key=lambda x: x[4])

    def find_text(self, query: str):
        results = self.search_items(query)
        display_results(results, self.headers)
        html_filename = 'output.html'
        export_to_html(results, self.headers, html_filename)
        print(f"Результаты поиска сохранены в файле: {html_filename}")

    def main(self, directory: str):
        self.load_prices(directory)
        while True:
            query = input("Введите текст для поиска (и 'exit' или 'выход' для завершения): ")
            if query.lower() in ['exit', 'выход']:
                print("Работа завершена.")
                break
            self.find_text(query)


def display_results(results: List[List], headers: List[str]):
    numbered_results = [[i + 1] + result for i, result in enumerate(results)]
    print(tabulate(numbered_results, headers=headers, tablefmt='grid'))


def export_to_html(results: List[List], headers: List[str], filename: str):
    numbered_results = [[i + 1] + result for i, result in enumerate(results)]
    table = tabulate(numbered_results, headers=headers, tablefmt='html')
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(table)


if __name__ == "__main__":
    pm = PriceMachine()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    pm.main(current_directory)
