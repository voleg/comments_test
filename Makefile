#!/usr/bin/make
DJANGO_PROJECT_NAME = comments_test



install:
	(cd $(DJANGO_PROJECT_NAME); pip install -r requirements.txt)

test:
	(cd $(DJANGO_PROJECT_NAME); python manage.py test)
