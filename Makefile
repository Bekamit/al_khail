run:
	python3 manage.py runserver
migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate
user:
	python3 manage.py createsuperuser
celery:
	celery -A core worker -l debug
redis:
	brew services start redis
redis-s:
	brew services stop redis
docker:
	docker-compose up -d --build