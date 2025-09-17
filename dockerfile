FROM python:3.12.3-slim-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc build-essential libpq-dev netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Добавим скрипт ожидания базы
COPY wait-for-db.sh /wait-for-db.sh
RUN chmod +x /wait-for-db.sh

# CMD ["/wait-for-db.sh", "db", "5432", "python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD sh -c "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn blog_project.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --timeout 60"
