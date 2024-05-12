import os
import time

directory = 'D:\\PythonProjectUniversity'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        file_size = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, путь: {filepath}, размер: {file_size} байт, время изменения: {formatted_time}, '
              f'родительская директория {parent_dir}')
