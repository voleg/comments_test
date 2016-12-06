An example comments backend
===========================

TODO
====

Part 1
------

#. Every comment binds to concrete user.
#. Comments could be created, edited or deleted.
#. Comments can not be deleted if there are any nested comments.
#. Comments has a tree structure, there are no limits on depth of nesting.
#. Every comment connected to some Entity (Blog post, other comment, etc) identified by object_type_id, object_id pair.
#. Service should provide interfaces for:
   - Create a comment, on some Entity (specifying some entity in request)
   - Edit a comment by ID
   - Get a first level comments with pagination
   - Extracting all child comments without nesting limits for given comment ID (the response to a client should be easily reconstructible including nesting)
   - Retrieving of full branch of comments by specifying a root, root could be an entity or a comment ID that is root for given branch
   - Retrieving a history of comments for given user
   - Dumping to a file (XML) of all comments history for user or for an entity in given date time interval. The response time for initial request must not depend on volume if data in resulting dump
   - Viewing a dump requests history with ability to re download same dump
#. Response time is limited to 1s

Part 2
------

#. Implement a history data storing (information on who and when some one edit/delete a comment and a comment diff) with ability to get this data for concrete comment
#. Implement an ability to subscribe to events on some entity comments (on comment create/edit/delete send a PUSH notification to client in the way client could represent it in interface)
#. For comments dump implement flexible mechanism with ability to add different file types

notes
-----
- there is no need in authentication/authorization in backend level, all user data may be transferred in request param 
- the relational DB should be used for this solution
