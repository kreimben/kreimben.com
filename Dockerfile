FROM python:3.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./database /code/database
COPY ./.instagram_token /code/.instagram_token
COPY ./configure.py /code/configure.py
COPY ./event.py /code/event.py
COPY main.py /code/main.py

EXPOSE 10120

CMD [ "python3", "main.py" ]
