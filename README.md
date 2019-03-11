# django-dance

## Docker setup

https://docs.docker.com/compose/django/

### Pre-check

Make sure MySQL port `3306` has not been allocated.

```bash
sudo lsof -i -P -n | grep 3306
```

- For Mac: `kill -9 <process id>`
- For Linux: `sudo kill <process id>`

### Create a Django project (NOT for deployment)

```bash
sudo docker-compose run web django-admin startproject api .
```

```bash
sudo docker-compose run web python manage.py startapp app
```

```bash
sudo docker-compose run web python manage.py migrate
sudo docker-compose run web python manage.py createsuperuser --email techlab@sydney.edu.au --username techlab
```

```bash
sudo docker-compose run web python manage.py makemigrations
sudo docker-compose run web python manage.py migrate
```

```bash
sudo docker-compose run web python manage.py test
```

### Start the initiated Django project

```bash
docker-compose up
```

### Stop the project, clean up containers and networks

```bash
docker-compose down
```

## Django REST framework

https://www.django-rest-framework.org/

## AWS auth backend for Django REST framework for AWS Cognito JWT tokens

https://github.com/LabD/django-cognito-jwt

## Other best practices

- Docker how to run pip requirements.txt only if there was a change?

https://stackoverflow.com/questions/34398632/docker-how-to-run-pip-requirements-txt-only-if-there-was-a-change