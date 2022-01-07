<p align="center">
  <br>
  <img width="200" height="200" src="extras/songmeta.png">
  <br><b>SongMeta</b>
</p>

## About

Fully functional example built on top of [aioli-flavors/rest-rdbms](https://github.com/aioli-flavors/rest-rdbms).

## Setting up

Requires Python 3.9+, Git, and Poetry.

### Building

```
$ git clone https://github.com/rbw/songmeta.git
$ cd songmeta
$ poetry update
```

## Starting Postgres

The application requires an SQLAlchemy-supported relational database. This example uses pg.ARRAY in AlbumModel, making it compatible with Postgres only.

A docker-compose file for running a Postgres server is available in the project root.

```
$ docker-compose up
```

## Starting SongMeta 

```
$ poetry shell
$ python -m songmeta
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
