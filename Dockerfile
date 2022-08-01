FROM python:3.10.5-bullseye

WORKDIR app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["hypercorn", "kreimben_com.asgi:application"]