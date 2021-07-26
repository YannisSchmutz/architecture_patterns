#!/bin/sh


echo "Waiting for postgres..."

while ! nc -z $HOSTEL_DB_HOST $CONFIG_DB_PORT; do
  sleep 0.1
done

echo "PostgreSQL started!"

exec "$@"

