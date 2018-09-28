# Part2 - Riak

## Common Query Caching

Curl request to add the top 5 queries to the 'QueryCache' bucket:

* ```curl -XPUT -H "Content-Type: text/json" -d "{ Quality Care Commission: 0,1,2,3,4,5,6 }" http://localhost:8098/buckets/QueryCache/keys/1```
* ```curl -XPUT -H "Content-Type: text/json" -d "{ September 2004: 9 }" http://localhost:8098/buckets/QueryCache/keys/2```
* ```curl -XPUT -H "Content-Type: text/json" -d "{ general population generally: 6,8 }" http://localhost:8098/buckets/QueryCache/keys/3```
* ```curl -XPUT -H "Content-Type: text/json" -d "{ Care Quality Commission admission: 1 }" http://localhost:8098/buckets/QueryCache/keys/4```
* ```curl -XPUT -H "Content-Type: text/json" -d "{ general population Alzheimer: 6 }" http://localhost:8098/buckets/QueryCache/keys/5```

Curl request to retrieve 'Care Quality Commission' saved query:

```curl -XGET -H "Content-Type: text/json" http://localhost:8098/buckets/QueryCache/keys/1```

This will return the JSON { Quality Care Commission: 0,1,2,3,4,5,6 }

## Monthly Indexes

N.B Secondary indexing did not work for my installation at first. I had to change the backend storage type to leveldb in /etc/riak/riak.conf first.

Curls requests to insert some data and indexes (I inserted record 1 that has a date of July to prove I was getting the correct keys back for June):

* ```curl -XPUT -H 'x-riak-index-date_bin: June 2013'   -H 'Content-Type: text/plain'   -d 'June 5 , 2013 : The majority of carers say they are extremely , very or quite satisfied with the support and services they and the person they care for receive'   http://localhost:8098/buckets/QueryCache/keys/0```

* ```curl -XPUT -H 'x-riak-index-date_bin: July 2013'   -H 'Content-Type: text/plain'   -d 'July 9 , 2013 : The HSCIC has extended the consultation period on a draft list of conditions to be included in a proposed Present on Admission flag '   http://localhost:8098/buckets/QueryCache/keys/1```

* ```curl -XPUT -H 'x-riak-index-date_bin: June 2013'   -H 'Content-Type: text/plain'   -d 'June 19 , 2013 : New figures from the Health and Social Care Information Centre ( HSCIC ) show in 2012 - 13 ( 2 ) almost two million patients were treated at the scene ( 3 ) by ambulance services without needing onward transportation'   http://localhost:8098/buckets/QueryCache/keys/2```

* ```curl -XPUT -H 'x-riak-index-date_bin: June 2013'   -H 'Content-Type: text/plain'   -d 'June 13 , 2013 : Almost one in five women who gave birth in the North East in 2012 - 13 classed themselves as a smoker when they had their baby , new figures show'   http://localhost:8098/buckets/QueryCache/keys/3```

* ```curl -XPUT -H 'x-riak-index-date_bin: June 2013'   -H 'Content-Type: text/plain'   -d 'June 5 , 2013 : The majority of carers say they are extremely , very or quite satisfied with the support and services they and the person they care for receive'   http://localhost:8098/buckets/QueryCache/keys/4```


Curl request to get keys 0,2,3,4

```curl -XGET http://localhost:8098/buckets/QueryCache/index/date_bin/June%202013```

## Version

I used Riak KV 2.2.3 on Ubuntu 18.04