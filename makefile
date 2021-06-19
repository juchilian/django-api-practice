DOCKER_YAML=-f docker-compose.yml
CI_DOCKER_YAML=-f docker-compose.yml.ci

DOCKER=docker-compose $(DOCKER_YAML)
DOCKER_CI=docker-compose $(CI_DOCKER_YAML)

GO_BUILD_IMAGE_NAME=go-built

build:
	$(DOCKER) build --parallel ${ARGS}

build-nocache:
	$(DOCKER) build --no-cache --parallel ${ARGS}

docker-up:
	$(DOCKER) up

exec-db:
	$(DOCKER) exec mysql bash

migrate-new:
	$(DOCKER) exec web python3 manage.py makemigrations

superuser:
	$(DOCKER) exec web python3 manage.py createsuperuser


