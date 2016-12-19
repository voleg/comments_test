An example comments backend
===========================

.. image:: https://travis-ci.org/voleg/comments_test.svg?branch=develop
    :target: https://travis-ci.org/voleg/comments_test

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
  Authorization: 1

  {
    'object_type': 'object.type',
    'object_id': 'id',
    'title': 'title',
    'body': 'body_text',
  }

  HTTP/1.1 200 OK
  Vary: Accept
  Content-Type: text/javascript

  { 'comment_id': 'id' }


`http POST localhost:8000/api/comment/ Authorization:'Token <token>' title='title' text='text' object_id='1' object_type='blog.post'`

Edit::

  PUT /api/comment-detail/<id> HTTP/1.1
  Host: example.com
  Accept: application/json, text/javascript
  Authorization: 1

  {
    'object_type': 'object.type',
    'object_id': 'id',
    'title': 'title',
    'body': 'body_text'
  }

  HTTP/1.1 200 OK
  Vary: Accept
  Content-Type: text/javascript

  { 'detail': 'OK' }

Delete::

  DELETE /api/comment-detail/<id> HTTP/1.1
  Host: example.com
  Accept: application/json, text/javascript
  Authorization: 1

  HTTP/1.1 200 OK
  Vary: Accept
  Content-Type: text/javascript

  { 'detail': 'OK' }

