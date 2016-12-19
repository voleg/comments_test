#!/usr/bin/make
DJANGO_PROJECT_NAME = comments_test



install:
	(cd $(DJANGO_PROJECT_NAME); python manage.py test)

test:
	(cd $(DJANGO_PROJECT_NAME); python manage.py test)
