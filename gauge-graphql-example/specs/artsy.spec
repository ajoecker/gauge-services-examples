# Artsy Graphql

* Given the endpoint "https://metaphysics-production.artsy.net"

## popular artists is matching
* When posting <file:src/test/resources/popular_artists.yml>
* Then "popular_artists.artists.name" is "Pablo Picasso, Banksy"

## popular artists contain matching
* When posting <file:src/test/resources/popular_artists.yml>
* Then "popular_artists.artists.name" contains "Pablo Picasso"

## popular artists contain multi matching
* When posting <file:src/test/resources/popular_artists.yml>
* Then "popular_artists.artists.name" contains "Pablo Picasso, Banksy"

## popular artists is matching with map to parse
* When posting <file:src/test/resources/popular_artists.yml>
* Then "popular_artists.artists" is "{name: Pablo Picasso, nationality: Spanish}, {name: Banksy, nationality: British}"

## popular artists is matching with table
* When posting <file:src/test/resources/popular_artists.yml>
* Then "popular_artists.artists" is 

   |name         |nationality|
   |-------------|-----------|
   |Pablo Picasso|Spanish    |
   |Banksy       |British    |

## popular artists contain matching with table
* When posting <file:src/test/resources/popular_artists.yml>
* Then "popular_artists.artists" contains 

   |name         |nationality|
   |-------------|-----------|
   |Pablo Picasso|Spanish    |
   |Banksy       |British    |
