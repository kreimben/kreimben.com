FROM pypy

WORKDIR app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 10120

ENTRYPOINT ["daphne", "-b", "0.0.0.0", "-p", "8000", "kreimben_com.asgi:application"]