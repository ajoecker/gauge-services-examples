# Deutsche Bahn QL

* Use "https://bahnql.herokuapp.com/graphql"

## station Frankfurt
* When posting <file:src/test/resources/dbahn_frankfurt.graphql>
* Then "stationWithEvaId.name" must be "Frankfurt (Main) Hbf"

## stations around Frankfurt with table
* When posting <file:src/test/resources/dbahn_frankfurt.graphql>
* And posting <file:src/test/resources/dbahn_frankfurt_nearby.graphql> with

   |name     |value                               |
   |---------|------------------------------------|
   |latitude |$stationWithEvaId.location.latitude |
   |longitude|$stationWithEvaId.location.longitude|
   |radius   |2000                                |
* Then "nearby.stations.name" must contain "Frankfurt (Main) Taunusanlage"

## stations around Frankfurt with string
* When posting <file:src/test/resources/dbahn_frankfurt.graphql>
* And posting <file:src/test/resources/dbahn_frankfurt_nearby.graphql> with "latitude:$stationWithEvaId.location.latitude, longitude:$stationWithEvaId.location.longitude, radius:2000"
* Then "nearby.stations.name" must contain "Frankfurt (Main) Taunusanlage"
