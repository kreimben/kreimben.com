FROM python:3.10-bullseye as builder

ARG PROJECT_PATH="/var/task/"

WORKDIR ${PROJECT_PATH}

# Install dependencies for mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# copy everything
COPY . ${PROJECT_PATH}

# install requirements
RUN pip install -r ${PROJECT_PATH}requirements.txt -t ${PROJECT_PATH}

# export zappa hanlder
# Grab the zappa handler.py and put it in the working directory
#RUN ZAPPA_HANDLER_PATH=$( \
#    python -c "from zappa import handler; print (handler.__file__)" \
#    ) \
#    && echo $ZAPPA_HANDLER_PATH \
#    && cp $ZAPPA_HANDLER_PATH ${PROJECT_PATH}

FROM public.ecr.aws/lambda/python:3.10

ARG PROJECT_PATH="/var/task/"

WORKDIR ${PROJECT_PATH}

COPY --from=builder ${PROJECT_PATH} ${PROJECT_PATH}

ENV ZAPPA_RUNNING_IN_DOCKER=True
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install mysqlclient in amazonlinux 2
RUN yum update && yum install mysql-devel gcc python3-devel yum install python3-pip -y
RUN pip install mysqlclient -t ${PROJECT_PATH}

EXPOSE 8000

#CMD [ "handler.lambda_handler" ]
CMD ["lambda_handler.application"]