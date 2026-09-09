import os

print("--- Приложение запущено ---")
# Проверяем, от какого пользователя работает процесс
print(f"Текущий UID процесса: {os.getuid()}")

# Проверяем доступность секретного ключа (для Шага 5)
secret_path = "/run/secrets/my_build_secret"
if os.path.exists(secret_path):
    with open(secret_path, "r") as f:
        print(f"Секрет успешно прочитан во время сборки: {f.read().strip()}")
