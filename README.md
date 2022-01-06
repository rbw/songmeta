<p align="center">
  <br>
  <img width="128" height="128" src="extras/records.png">
  <br><b>Records</b>
</p>


## Setting up

Requires Python 3.9+, git, and poetry.

### Building

```
$ git clone https://github.com/rbw/records.git
$ cd records
$ poetry update
```

### Starting Postgres

The application requires an SQLAlchemy-supported relational database. This example uses pg.ARRAY in AlbumModel, making it compatible with Postgres only.

A docker-compose file for running a Postgres server is available in the project root.

```
$ docker-compose up
```

### Starting Records 

```
$ poetry shell
$ python -m records
```

## Usage

### Get all albums
```
$ curl http://localhost:5000/albums
```

### Create an album
```
$ curl -X POST --data '{"title": "test", "release_date": "2035-01-20", "stores": ["APPLE", "YOUTUBE"], "tracks": ["TEST000000001", "TEST000000002"], "upc": "00000000000005"}' http://localhost:5000/albums
```

### Show an album
```
$ curl http://localhost:5000/albums/00000000000005
```
