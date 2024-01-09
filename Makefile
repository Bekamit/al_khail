# Определение переменных
COMPOSE = docker-compose
APP_SERVICE = api

# Цель для сборки Docker-образов
build:
    $(COMPOSE) build

# Цель для запуска всех сервисов
up:
    $(COMPOSE) up -d

# Цель для остановки и удаления контейнеров
down:
    $(COMPOSE) down

# Цель для перезапуска приложения
restart:
    $(COMPOSE) restart $(APP_SERVICE)

# Цель для выполнения миграций
migrate:
    $(COMPOSE) exec $(APP_SERVICE) sh -c "python3 manage.py makemigrations && python3 manage.py migrate"

# Цель для просмотра логов приложения
logs:
    $(COMPOSE) logs -f $(APP_SERVICE)

user:
    sh -c "docker exec -it al_khail-backend-api-1 python3 manage.py createsuperuser"