# Deutsche Bahn QL

* Given the endpoint "https://bahnql.herokuapp.com/graphql"

## station Frankfurt
* When posting <file:src/test/resources/dbahn_frankfurt.yml>
* Then "stationWithEvaId.name" is "Frankfurt (Main) Hbf"
* And the request finished in less than "5000" ms

## stations around Frankfurt with table
* When posting <file:src/test/resources/dbahn_frankfurt.yml>
* And posting <file:src/test/resources/dbahn_frankfurt_nearby.yml>
* Then "nearby.stations.name" contains "Frankfurt (Main) Taunusanlage"

