# Json Place Holder

* Given the endpoint "https://jsonplaceholder.typicode.com/"
* Set "email" to "Nikita@garfield.biz"

## Comments with id and table
* When getting "comments" with

   |name  |value|
   |------|-----|
   |postId|1    |
* And extracting "id" where "email=%email%"
* Then "id" is "3"

## Comments with id and inline text
* When getting "comments" with "postId=1"
* And extracting "id" where "email=Nikita@garfield.biz"
* Then "id" is "3"

## Putting
* When putting <file:src/test/resources/jsonplaceholder_put.json> to "posts/50"
* Then status code is "200"