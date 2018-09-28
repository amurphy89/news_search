# Part2 - Riak

## Common Query Caching

Curl Requests to add the top 5 queries to the 'QueryCache' bucket:

* ```curl -XPUT -H "Content-Type: text/json" -d "{ Quality Care Commission: 0,1,2,3,4,5,6 }" http://localhost:8098/buckets/QueryCache/keys/1```
* ```curl -XPUT -H "Content-Type: text/json" -d "{ September 2004: 9 }" http://localhost:8098/buckets/QueryCache/keys/2```
* ```curl -XPUT -H "Content-Type: text/json" -d "{ general population generally: 6,8 }" http://localhost:8098/buckets/QueryCache/keys/3```
* ```curl -XPUT -H "Content-Type: text/json" -d "{ Care Quality Commission admission: 1 }" http://localhost:8098/buckets/QueryCache/keys/4```
* ```curl -XPUT -H "Content-Type: text/json" -d "{ general population Alzheimer: 6 }" http://localhost:8098/buckets/QueryCache/keys/5```