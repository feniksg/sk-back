include env
export DEBUG := 1
TOPDIR = $(shell pwd)


start-frontend-local:
	docker build -t node:latest -f Dockerfile_frontend .
	docker-compose --file docker-compose-local-frontend.yml up -d nuxt-lucky_dress

start-backend-local:
	docker build -t skrollik:alpha -f Dockerfile_backend .
	docker-compose --file docker-compose-local-backend.yml -p skrollik --env-file ./env up -d --remove-orphans
	docker-compose --file docker-compose-local-backend.yml logs -t -f app

