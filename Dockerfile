FROM python:3.7

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./database /code/database
COPY ./app /code/app

EXPOSE 10120

CMD [ "python3", "./app/main.py" ]
