up:
	docker-compose -f local.yml up

up-build:
	docker-compose -f local.yml up --build

test:
	docker-compose -f local.yml run --rm django pytest

bash:
	docker-compose -f local.yml run --rm django bash

shell:
	docker-compose -f local.yml run --rm django python manage.py shell
