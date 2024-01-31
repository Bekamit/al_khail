install:
    sudo apt install docker-compose \
    && sudo usermod -aG docker $(whoami) \
    && sudo service docker restart

rm:
    docker-compose stop \
    && docker-compose rm \
#   && sudo rm -rf pgdata/

up:
    docker-compose up -d --build

down:
    docker-compose down -v

recreate:
    docker-compose up -d --force-recreate

up-ssl:
    docker-compose -f docker-compose-ssl.yaml up -d --build

down-ssl:
    docker-compose -f docker-compose-ssl.yaml up down -v

recreate-ssl:
    docker-compose -f docker-compose-ssl.yaml up -d --force-recreate
