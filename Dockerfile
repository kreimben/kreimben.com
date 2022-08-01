FROM python:3.10.5-bullseye




RUN ['hypercorn', 'myproject.asgi:application']