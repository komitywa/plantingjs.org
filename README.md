PLANTINGJS.ORG
====

[![Join the chat at https://gitter.im/komitywa/plantingjs.org](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/komitywa/plantingjs.org?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


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
