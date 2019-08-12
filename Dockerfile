# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7-alpine

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /pat

# Set the working directory to /music_service
WORKDIR /pat

# Copy the current directory contents into the container at /allarmi
ADD ./ /pat/

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

COPY ./bin/docker_start.sh /start.sh

RUN chmod +x /start.sh

# ENV DJANGO_SETTINGS_MODULE=AllarmiWs.settings.deploy

# Run startup file
ENTRYPOINT [ "/start.sh" ]
