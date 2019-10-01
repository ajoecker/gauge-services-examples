# Artsy Graphql

* Use "https://metaphysics-production.artsy.net"

## popular artists must be matching
* When posting <file:src/test/resources/popular_artists.graphql>
* Then "popular_artists.artists.name" must be "Pablo Picasso, Banksy"

## popular artists contain matching
* When posting <file:src/test/resources/popular_artists.graphql>
* Then "popular_artists.artists.name" must contain "Pablo Picasso"

## popular artists contain multi matching
* When posting <file:src/test/resources/popular_artists.graphql>
* Then "popular_artists.artists.name" must contain "Pablo Picasso, Banksy"

## popular artists must be matching with map to parse
* When posting <file:src/test/resources/popular_artists.graphql>
* Then "popular_artists.artists" must be "{name: Pablo Picasso, nationality: Spanish}, {name: Banksy, nationality: British}"

## popular artists contain matching with map to parse
* When posting <file:src/test/resources/popular_artists_variable.graphql> with "size:4"
* Then "popular_artists.artists" must contain "{name: Pablo Picasso, nationality: Spanish}"

## popular artists contain matching with table to parse
* When posting <file:src/test/resources/popular_artists_variable.graphql> with 

   |name|value|
   |----|-----|
   |size|4    |
* Then "popular_artists.artists" must contain "{name: Pablo Picasso, nationality: Spanish}"

## popular artists must be matching with table
* When posting <file:src/test/resources/popular_artists.graphql>
* Then "popular_artists.artists" must be 

   |name         |nationality|
   |-------------|-----------|
   |Pablo Picasso|Spanish    |
   |Banksy       |British    |

## popular artists contain matching with table
* When posting <file:src/test/resources/popular_artists.graphql>
* Then "popular_artists.artists" must contain 

   |name         |nationality|
   |-------------|-----------|
   |Pablo Picasso|Spanish    |
   |Banksy       |British    |
