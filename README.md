# sqlalchemy-orm

Working examples from https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/

## Quickstart

* Run `docker-compose up`
* Configure db through pgadmin (described under "Postgresql & PgAdmin powered by compose" further down below)
* Run:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt

python src/inserts.py  # populate the database
python src/queries.py  # perform queries
```

Output from `queries.py`:

```
### All movies:
The Bourne Identity was released on 2002-10-11
Furious 7 was released on 2015-04-02
Pain & Gain was released on 2013-08-23

### Recent movies:
Furious 7 was released after 2015

### Dwayne Johnson movies:
The Rock starred in Pain & Gain
The Rock starred in Furious 7

### Actors that live in Glendale:
Dwayne Johnson has a house in Glendale
Mark Wahlberg has a house in Glendale
```

## Notes on SQLAlchemy ORM

* SQLAlchemy expose interfaces in accordance with the Python DBAPI, specified in [PEP-249](https://www.python.org/dev/peps/pep-0249/)
* PostgreSQL, MySQL, Oracle, Microsoft SQL Server, and SQLite can be used with SQLAlchemy
* Psycopg fully implements the Pyhton DBAPI implementation for PostgreSQL
* SQLAlchemy supports various [SQL dialects](http://docs.sqlalchemy.org/en/latest/dialects/)
* SQLAlchemy supports [generic types](https://docs.sqlalchemy.org/en/14/core/type_basics.html#generic-types), [vendor types](https://docs.sqlalchemy.org/en/14/core/type_basics.html#sql-standard-and-multiple-vendor-types) and [custom types](https://docs.sqlalchemy.org/en/14/core/custom_types.html)
* SQLAlchemy supports four types of relationships:
  * [One to many](http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#one-to-many)
  * [Many to one](http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#many-to-one)
  * [One to one](http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#one-to-one)
  * [Many to many](http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#many-to-many)
* SQLAlchemy ORM [cascading](http://docs.sqlalchemy.org/en/latest/orm/cascades.html) are handled through the `relationship()` construct. The most common cascade strategies:
  * `save-update`: Indicates that when a parent object is saved/updated, child objects are saved/updated as well.
  * `delete`: Indicates that when a parent object is deleted, children of this object will be deleted as well.
  * `delete-orphan`: Indicates that when a child object loses reference to a parent, it will get deleted.
  * `merge`: Indicates that merge() operations propagate from parent to children.
* SQLAlchemy ORM [sessions](http://docs.sqlalchemy.org/en/rel_1_1/orm/session_basics.html) is used to maintain a list of objects affected by a business transaction and to coordinate the writing out of these changes

# Postgresql & PgAdmin powered by compose

This part of the project was forked from: https://github.com/khezen/compose-postgres

## Requirements:
* docker >= 17.12.0+
* docker-compose

## Quick Start
* Clone or download this repository
* Go inside of directory,  `cd compose-postgres`
* Run this command `docker-compose up -d`

## Environments
This Compose file contains the following environment variables:

* `POSTGRES_USER` the default value is **postgres**
* `POSTGRES_PASSWORD` the default value is **changeme**
* `PGADMIN_PORT` the default value is **5050**
* `PGADMIN_DEFAULT_EMAIL` the default value is **pgadmin4@pgadmin.org**
* `PGADMIN_DEFAULT_PASSWORD` the default value is **admin**

## Access to postgres: 
* `localhost:5432`
* **Username:** postgres (as a default)
* **Password:** changeme (as a default)

## Access to PgAdmin: 
* **URL:** `http://localhost:5050`
* **Username:** pgadmin4@pgadmin.org (as a default)
* **Password:** admin (as a default)

## Add a new server in PgAdmin:
* **Host name/address** `postgres`
* **Port** `5432`
* **Username** as `POSTGRES_USER`, by default: `postgres`
* **Password** as `POSTGRES_PASSWORD`, by default `changeme`