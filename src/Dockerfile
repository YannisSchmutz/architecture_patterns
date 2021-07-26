# pull official base image
FROM python:3.8.3-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD requirements/ /requirements/

# install system dependencies and python dependencies
RUN set -ex \
  && apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean \
  && pip install --upgrade pip \
  && pip install -r requirements/dev.txt


RUN mkdir /code
ADD . /code/

# set working directory
WORKDIR /code

EXPOSE 6000
# run entrypoint.sh
RUN chmod a+x entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
