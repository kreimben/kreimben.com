FROM python:3.10-bullseye

WORKDIR app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 10120

CMD [ "python3", "./app/main.py" ]
