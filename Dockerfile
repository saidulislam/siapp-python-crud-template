# pull official base image
FROM python:3.10.1-slim-buster

# set environment variables
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr
# INSTALL_PATH: application path inside the container
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV INSTALL_PATH /siapp

# set working directory
WORKDIR $INSTALL_PATH

# add and install requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# add siapp
COPY . .

# run the server
CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "siapp.app:create_app()"