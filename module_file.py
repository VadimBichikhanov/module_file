import os
import time

# Укажите путь к директории, которую нужно обойти
directory = "."

# Используем os.walk для обхода каталога
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формируем полный путь к файлу
        filepath = os.path.join(root, file)
        
        # Получаем время последнего изменения файла
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        
        # Получаем размер файла
        filesize = os.path.getsize(filepath)
        
        # Получаем родительскую директорию файла
        parent_dir = os.path.dirname(filepath)
        
        # Выводим информацию о файле
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
