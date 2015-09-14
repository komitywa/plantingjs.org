## Synopsis

Flask-based application that run http://plantingjs.org

## Installation

Development enviroment could be easly created using Docker Compose file available in repository.

For these, that don't want to use Docker:
* Download this repository
* Download and build [plantingjs](https://github.com/komitywa/plantingjs)
* Put /dist directory from plantingjs into /src/static/plantingjs
* Install Flask
* Create database (Sqlite file will be create in direct parent of repository's root directory) and make it writable by user that will run app
* Configure Apache (WSGI file is included, You need to add access to directory that contains database)
