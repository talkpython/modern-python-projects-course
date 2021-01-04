.PHONY: init build run unittest test

TODO: Update this makefile and remove unused stuff
help:
	@echo "init - set up the application"
	@echo "build - build Docker containers"
	@echo "run - start Docker containers"
	@echo "test - run all tests"
	@echo "unittest - run unit tests only"


init:
	make build
	make run
	docker-compose exec web simple db upgrade
	docker-compose exec web simple db migrate

build:
	docker-compose build

run:
	docker-compose up -d

unittest:
	pytest -vv -m unit --no-cov

test:
	pytest tests

