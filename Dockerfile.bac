FROM python:3.11

WORKDIR app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

# celery -A kreimben_com worker -l info
# daphne -b 0.0.0.0 -p 8000 kreimben_com.asgi:application