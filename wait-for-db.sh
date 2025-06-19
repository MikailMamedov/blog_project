#!/bin/sh

# wait-for-db.sh

set -e

host="$1"
port="$2"
shift 2

echo "Ожидание доступности базы данных $host:$port..."

while ! nc -z "$host" "$port"; do
  echo "База данных недоступна, ждем..."
  sleep 1
done

echo "База данных доступна, запускаем приложение..."

exec "$@"
