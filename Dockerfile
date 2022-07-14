FROM python:3.10-bullseye

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 10120

CMD [ "python3", "./app/main.py" ]
