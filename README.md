# Explore Your Data - with AI 🦾
[![Build Status](https://travis-ci.com/LRS4/explore-your-data.svg?branch=master)](https://travis-ci.com/LRS4/explore-your-data.svg?branch=master)   [![codecov](https://codecov.io/gh/LRS4/explore-your-data/branch/master/graph/badge.svg)](https://codecov.io/gh/LRS4/explore-your-data)


## Introduction
An application to present exploratory data analysis in an accessible format. You bring a nicely formatted CSV file that has some data in it, and let the AI worry about the rest! It will give you a good overview of the data for quicker understanding, perfect for data professionals and non-technical persons alike.

![Vue Logo](/docs/vue-logo.png "Vue Logo") ![Flask Logo](/docs/flask-logo.png "Flask Logo")

## Features
* [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) 1.0 App
* [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/index.html)
* [Flask-RestPlus](http://flask-restplus.readthedocs.io) API with class-based secure resource routing
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) ORM
* [PyTest](http://pytest.org) test suite
* [vue-cli 3](https://github.com/vuejs/vue-cli/blob/dev/docs/README.md) + yarn
* [Vuex](https://vuex.vuejs.org/)
* [Vue Router](https://router.vuejs.org/)
* [Axios](https://github.com/axios/axios/) for backend communication
* [Postgres](https://www.postgresql.org/) database using [ElephantSQL](https://www.elephantsql.com/)
* [Psycopg2](https://pypi.org/project/psycopg2/) PostgreSQL database adapter
* Vue [Filters](https://vuejs.org/v2/guide/filters.html)
* [Travis CI](https://travis-ci.com/github/LRS4/explore-your-data) pipeline with automated testing
* [Codecov](https://codecov.io/gh/LRS4/explore-your-data) for monitoring code test coverage
* [Heroku](https://www.heroku.com/) Configuration with automated Git deployment + Gunicorn

## Structure

Uses Flask & Flask-RESTX (fork of Flask-RestPlus) to create a minimal REST style API,
and let's VueJs + vue-cli handle the front end and asset pipline.
Data from the python server to the Vue application is passed by making AJAX requests with Axios.

### Application Structure

#### Rest Api

The Api is served using a Flask blueprint at `/api/` using Flask RESTX (fork of Flask-RestPlus) class-based
resource routing.

#### Client Application

A Flask view is used to serve the `index.html` as an entry point into the Vue app at the endpoint `/`.

The template uses vue-cli 3 and assumes Vue Cli & Webpack will manage front-end resources and assets, so it does overwrite template delimiter.

The Vue instance is preconfigured with Filters, Vue-Router, Vuex; each of these can easilly removed if they are not desired.

#### Important Files

| Location             |  Content                                   |
|----------------------|--------------------------------------------|
| `/app`               | Flask Application                          |
| `/app/api`           | Flask Rest Api (`/api`)                    |
| `/app/client.py`     | Flask Client (`/`)                         |
| `/src`               | Vue App .                                  |
| `/src/main.js`       | JS Application Entry Point                 |
| `/public/index.html` | Html Application Entry Point (`/`)         |
| `/public/static`     | Static Assets                              |
| `/dist/`             | Bundled Assets Output (generated at `yarn build` |


## Installation

##### Before you start

Before getting started, you should have the following installed and running:

- [X] Yarn - [instructions](https://yarnpkg.com/en/docs/install#mac-stable)
- [X] Vue Cli 3 - [instructions](https://cli.vuejs.org/guide/installation.html)
- [X] Python 3
- [X] Pipenv (optional)
- [X] Heroku Cli (if deploying to Heroku)

##### Dependencies

* Setup virtual environment, install dependencies, and activate it:

	```
	$ pipenv install --dev
	$ pipenv shell
	```

* Install JS dependencies

	```
	$ yarn install
	```


## Development Server

Add a `.env` file for following environment variables:


Run Flask Api development server:

```
$ python run.py
```

From another tab in the same directory, start the webpack dev server:

```
$ yarn serve
```

The Vuejs application will be served from `localhost:8080` and the Flask Api
and static files will be served from `localhost:5000`.

The dual dev-server setup allows you to take advantage of
webpack's development server with hot module replacement.

Proxy config in `vue.config.js` is used to route the requests
back to Flask's Api on port 5000.

If you would rather run a single dev server, you can run Flask's
development server only on `:5000`, but you have to build build the Vue app first
and the page will not reload on changes.

```
$ yarn build
$ python run.py
```


## Production Server

This template is configured to work with Heroku + Gunicorn and it's pre-configured
to have Heroku build the application before releasing it.

#### JS Build Process

Heroku's nodejs buildpack will handle install for all the dependencies from the `packages.json` file.
It will then trigger the `postinstall` command which calls `yarn build`.
This will create the bundled `dist` folder which will be served by whitenoise.

#### Python Build Process

The python buildpack will detect the `Pipfile` and install all the python dependencies.
To add new python dependencies, once in the virtual environment using `pipenv shell` run

	```
	$ pipenv install <package-name>
	$ pipenv lock
	```
To remove a python dependency, use `pipenv uninstall <package-name>`

Then update the .travis.yml with the new packages under `install`, to ensure the build pipeline doesn't fail.

#### Running tests

To run all pytest unit tests run `pytest` or `pytest tests/`

#### Production Server Setup

Here are the commands we need to run to get things setup on the Heroku side:

	```
	$ heroku apps:create flask-vuejs-template-demo
	$ heroku git:remote --app flask-vuejs-template-demo
	$ heroku buildpacks:add --index 1 heroku/nodejs
	$ heroku buildpacks:add --index 2 heroku/python
	$ heroku config:set FLASK_ENV=production
	$ heroku config:set FLASK_SECRET=SuperSecretKey

	$ git push heroku
	```

### References
Credit for the Vue.js Flask template goes to [gtalarico](https://github.com/gtalarico/flask-vuejs-template) and set up to [this video](https://www.youtube.com/watch?v=VZv8UybZHNA).

* [Managing python dependencies](https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv)
* [Using yarn](https://stackoverflow.com/questions/47238241/heroku-build-failing-due-to-yarn-and-npm-lockfile-conflict)
* [Upgrading yarn packages](https://classic.yarnpkg.com/en/docs/cli/upgrade/)
* [Initialise SQLAlchemy](https://stackoverflow.com/questions/45228328/sqlalchemy-nameerror-name-db-is-not-defined)
* [Python garbage collection](https://stackify.com/python-garbage-collection/#:~:text=The%20Python%20garbage%20collector%20has,a%20threshold%20number%20of%20objects)
* [Pandas optional dependencies](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html#optional-dependencies)