FROM cr.yandex/mirror/library/python:3.11-slim

WORKDIR /app

RUN useradd -r -U appuser

COPY . .

RUN --mount=type=secret,id=my_secret \
    if [ -f /run/secrets/my_secret ]; then \
        echo "Секрет доступен при сборке:"; \
        cat /run/secrets/my_secret; \
    else \
        echo "Секрет не передан"; \
    fi

RUN chown -R appuser:appuser /app

USER appuser

CMD ["python", "app.py"]
