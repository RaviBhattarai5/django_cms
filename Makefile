.PHONY: install
install:
	poetry install

.PHONY: run-server
run-server:
	poetry run python manage.py runserver

.PHONY: migrations
migrations:
	poetry run python manage.py makemigrations
	
.PHONY: migrate
migrate:
	poetry run python manage.py migrate
