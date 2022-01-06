# rest-dbms: HTTP/REST+RDBMS Flavor

Aioli Flavor For building HTTP/REST APIs with support for relational databases.

### Core Components

| Name        | Description                     |
|-------------|---------------------------------|
| controller  | Abstract Controller class       |
| controllers | Package of concrete Controllers |
| service     | Abstract Service class          |
| services    | Package of concrete Services    |
| database    | Database package                |


### Database Package

| Name        | Description                      |
|-------------|----------------------------------|
| manager     | Module for managing the database |
| service     | Database Service mixin           |
| table       | Abstract Table Model             |
| tables      | Package of concrete Tables       |
