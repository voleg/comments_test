An example comments backend
===========================

Iterations
----------

1. Choosing a technology stack:

This could be done in various ways ...

- asynio, aiohttp, sqlalchemy, aiopg
- flask, flask-restfull, sqlalchemy
- django, djangorestframework


2. Design the way tree structures could be stored in SQL

- sqlalchemy-mptt
- django-mptt
- django-treebeard


3. API design:

Create API::

  POST /api/comment/ HTTP/1.1
  Host: example.com
  Accept: application/json, text/javascript
  X-Token: 1

  {
    'object_name': 'name',
    'object_id': 'id',
    'title': 'title',
    'body': 'body_text',
  }

  HTTP/1.1 200 OK
  Vary: Accept
  Content-Type: text/javascript

  { 'comment_id': 'id' }


Edit::

  PUT /api/comment/<id>/edit HTTP/1.1
  Host: example.com
  Accept: application/json, text/javascript
  X-Token: 1

  {
    'object_name': 'name',
    'object_id': 'id',
    'title': 'title',
    'body': 'body_text'
  }

  HTTP/1.1 200 OK
  Vary: Accept
  Content-Type: text/javascript

  { 'detail': 'OK' }

Delete::

  DELETE /api/comment/<id> HTTP/1.1
  Host: example.com
  Accept: application/json, text/javascript
  X-Token: 1

  HTTP/1.1 200 OK
  Vary: Accept
  Content-Type: text/javascript

  { 'detail': 'OK' }

