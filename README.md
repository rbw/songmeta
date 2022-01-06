# flavor-base: Aioli Base Flavor

Provides a Base Flavor that currently makes use of [Starlette](https://www.starlette.io) for connection 
handling and [Marshmallow](https://marshmallow.readthedocs.io/en/stable) for data serialization, but offers no 
external API.

#### Flavor Structure

Most Flavors implements a three-layer architecture with a separation between the Transport, Domain, and Data layers, 
which should be suitable for most applications.

#### Official Flavors (1)

- [aioli-flavors/rest-rdbms](https://github.com/aioli-flavors/rest-rdbms): RESTful HTTP API, RDBMS support
