# Используем базовый образ python:3.11-slim
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы приложения (app.py и requirements.txt) в контейнер
COPY . /app

# Устанавливаем зависимости из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 5000 для связи
EXPOSE 5000

# Задаем команду для запуска приложения
CMD ["python", "app.py"]
