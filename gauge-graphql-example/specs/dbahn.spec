# Deutsche Bahn QL

* Use "https://bahnql.herokuapp.com/graphql"

## station Frankfurt
* When sending <file:src/test/resources/dbahn_frankfurt.graphql>
* Then "stationWithEvaId.name" must be "Frankfurt (Main) Hbf"

## stations around Frankfurt with table
* When sending <file:src/test/resources/dbahn_frankfurt.graphql>
* And sending <file:src/test/resources/dbahn_frankfurt_nearby.graphql> with

   |name     |value                               |
   |---------|------------------------------------|
   |latitude |$stationWithEvaId.location.latitude |
   |longitude|$stationWithEvaId.location.longitude|
   |radius   |2000                                |
* Then "nearby.stations.name" must contain "Frankfurt (Main) Taunusanlage"

## stations around Frankfurt with string
* When sending <file:src/test/resources/dbahn_frankfurt.graphql>
* And sending <file:src/test/resources/dbahn_frankfurt_nearby.graphql> with "latitude:$stationWithEvaId.location.latitude, longitude:$stationWithEvaId.location.longitude, radius:2000"
* Then "nearby.stations.name" must contain "Frankfurt (Main) Taunusanlage"
