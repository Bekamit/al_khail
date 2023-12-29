## Use the official Python 3.11 image
#FROM python:3.11
#
## Set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
## Set the working directory to /app
#WORKDIR /app
#
## Copy the requirements file into the container
#COPY work.txt /app/
#RUN pip install --upgrade pip && pip install -r work.txt
#
## Copy all the project files into the container
#COPY . /app/
#
## Optionally: Collect static files
## RUN python manage.py collectstatic --noinput
#
## Start the Django server using Gunicorn
##CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Core.wsgi:application"]
#CMD python3 manage.py makemigrations --noinput && \
#    python3 manage.py migrate --noinput && \
#    gunicorn -b 0.0.0.0:8000 Core.wsgi

FROM python:3.11-alpine

WORKDIR /usr/src/app

EXPOSE 8000

COPY work.txt ./

COPY . .

RUN pip install --no-cache-dir -r work.txt && python3 manage.py collectstatic && python3 manage.py makemigrations && python3 manage.py migrate
