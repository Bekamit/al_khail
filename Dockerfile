
FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

EXPOSE 9000

COPY requirements/prod.txt ./

COPY . .

#CMD ["mv", ".env", ".env.local"]
#CMD ["mv", ".env.prod", ".env"]

RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r prod.txt && python3 manage.py collectstatic --noinput
