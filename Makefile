run:
	python3 manage.py runserver
user:
	python3 manage.py createsuperuser
migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate
celery:
	celery -A config worker -l debug
redis:
	brew services start redis
redis-stop:
	brew services stop redis
