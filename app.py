import os
import sys

def main():
    # Чтение переменных окружения
    app_env = os.getenv("APP_ENV", "development")
    secret_key = os.getenv("SECRET_KEY", "default_key")
    db_url = os.getenv("DATABASE_URL", "sqlite:///default.db")

    print(f"--- ЗАПУСК ПРИЛОЖЕНИЯ ---")
    print(f"Текущее окружение (APP_ENV): {app_env}")
    print(f"Секретный ключ (SECRET_KEY): {secret_key}")
    print(f"База данных (DATABASE_URL): {db_url}")

    # Пример адаптации поведения (выбор режима отладки)
    if app_env.startswith("production"):
        print("РЕЖИМ: Продакшн. Отладка отключена, логирование в строгом режиме.")
    else:
        print("РЕЖИМ: Разработка. Включен детальный вывод ошибок (Debug).")

if __name__ == "__main__":
    main()