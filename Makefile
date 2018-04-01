mysql:
	docker-compose run --rm db mysql -hdb -uroot -prootpassword -Dtest

redis-cli:
	docker-compose run --rm cache redis-cli -h cache

restart-web:
	docker-compose up -d --no-deps web

recreate-web:
	docker-compose up -d --no-deps --build web
