# command to install --> make install
.PHONY: install
install:
	poetry install

# command to run server --> make run-server
.PHONY: run server
run server:
	poetry run python manage.py runserver

# command to make migrations --> make migrations
.PHONY: migrations
migrations:
	poetry run python manage.py makemigrations
	
# command to migrate --> make migrate
.PHONY: migrate
migrate:
	poetry run python manage.py migrate

# To create app under master run command --> make master app_name
.PHONY: master
master:
	$(eval name := $(wordlist 2,2,$(MAKECMDGOALS)))
	@echo "Creating master app: $(name)"
	@mkdir -p apps/master/$(name); \
	poetry run django-admin startapp $(name) apps/master/$(name); \
	touch apps/master/$(name)/urls.py; \
	touch apps/master/$(name)/forms.py

%:
	@:

# To create app under any directory  --> make app path/to/the/folder/app_name
.PHONY: app
app:
	$(eval dir := $(wordlist 2,2,$(MAKECMDGOALS)))
	@echo "Creating app in: $(dir)"
	@mkdir -p $(dir); \
	poetry run django-admin startapp $(notdir $(dir)) $(dir); 

%:
	@: