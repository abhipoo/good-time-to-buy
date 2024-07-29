docker-compose -f docker-compose.yml down -v
docker-compose -f docker-compose.yml up -d

docker exec -it good-time-to-buy-db-1 /bin/bash