
FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

EXPOSE 8000

COPY requirements/work.txt ./

COPY . /app/
#COPY . .

RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r work.txt && python3 manage.py collectstatic --noinput
