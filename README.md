<p align="center">
  <br>
  <img width="128" height="128" src="extras/flavors.png">
  <br><b>Aioli rest-rdbms Flavor</b>
</p>

Aioli Flavor For building a RESTful API with support for relational databases. 


##### Core Components

| Name        | Description                     |
|-------------|---------------------------------|
| controller  | Abstract Controller class       |
| controllers | Package of concrete Controllers |
| service     | Abstract Service class          |
| services    | Package of concrete Services    |
| database    | Database package                |


##### Database Package

| Name        | Description                      |
|-------------|----------------------------------|
| manager     | Module for managing the database |
| service     | Database Service mixin           |
| table       | Abstract Table Model             |
| tables      | Package of concrete Tables       |
