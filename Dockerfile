# Start with a python3 image
FROM python:3
 
ENV PYTHONUNBUFFERED 1

# Update
RUN apt-get update

RUN mkdir /code
WORKDIR /code

# Install requirements
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/