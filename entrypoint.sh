echo "Применяем миграции..."
python manage.py migrate --noinput

echo "Собираем статику..."
python manage.py collectstatic --noinput

echo "Запускаем Gunicorn..."
gunicorn blog_project.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --timeout 60