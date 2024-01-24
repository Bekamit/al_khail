install:
	sudo apt install docker-compose \
	&& sudo usermod -aG docker $$USER \
	&& sudo service docker restart


rm:
	docker-compose stop \
	&& docker-compose rm \
# 	&& sudo rm -rf pgdata/

up:
    docker-compose up -d --build

down:
    docker-compose down -v

recreate:
	docker-compose up -d --force-recreate
