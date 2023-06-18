FROM python:3.11-alpine

WORKDIR app
COPY . /app

RUN apk update \
    && apk add gcc musl-dev mariadb-connector-c-dev libffi-dev
RUN pip install mysqlclient

RUN pip install -r requirements.txt

EXPOSE 8000

#ENTRYPOINT ["celery", "-A", "kreimben_com", "worker", "-l", "info", "&","daphne", "-b", "0.0.0.0", "-p", "8000", "kreimben_com.asgi:application"]