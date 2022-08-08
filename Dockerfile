FROM python:3.10.5-bullseye

WORKDIR app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 10120

CMD ["cp", "-r", "/app/static_ready/*", "/app/static/", "&&", "daphne", "-b", "0.0.0.0", "-p", "8000", "kreimben_com.asgi:application"]