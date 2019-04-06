# postcards-tests

## Installation

Run `yarn install` to install all the packages listed in `package.json`.

## API testing

API testing is done using Postman and Newman (the Postman CLI).

### Prerequisites

The following should be true:

- you have a Postman collection to run
- you have a Postman environment configuring the variables used in the collection
- the application is deployed on Heroku

#### Tests > requests > collections

Postman uses the concepts of tests, requests and collections. Tests are linked to the request they test and multiple requests are bundled in collections.

To avoid having to copypaste values you can define an environment.

#### No standard automated export from Postman

Most of the times you first write the test in Postman since it allows you to interactively modify the test. However, tests created in Postman can't be automatically exported as collections in an easy way. The `newman` CLI [doesn't offer](https://github.com/postmanlabs/postman-app-support/issues/2691) any functionality to do this.

Another problem is exporting environments. There's no way to have Postman export the environment with variables values included. So we don't automatically export it but manually export it from within Postman and then define the values for the variables. This has only to be done when we use variables we didn't use before.

#### Workaround to export tests in a semi-automatic way

Since manually exporting the tests each time you push a commit is a hassle we still need a somewhat automated approach. A request is sent to the Postman API to retrieve the latest version of the collection using a python script `export_postman_collection.py`.

An API key (`postman_api_key`) and collection uid (`collection_uid`) of the collection are necessary to send the request. Both of these are in the `secrets.py` file. This file is ignored by git for security reasons.

The script requires `Python 3` and the `requests` library. So to succesfully launch the script we need to:

- set up a `Python 3` virtual environment
- install a version of `requests` as defined in the `requirements.txt` file
- run the script itself

A small shell script `./export_postman_collection.sh` combining the steps above has been added. Make sure to run this shell script before commiting your code so you use the latest versions of the tests.

### Running the tests

Tests can be run in two ways:

- from the command line
- on CI using Travis

Run from the command line: `newman run postcards_postman_collection.json`.

## E2E testing

E2E testing is done with Cypress.

### Running the tests

Cypress can be ran in 2 modes:

- headless: `yarn run cypress:run`
- debug: `yarn run cypress:open`

The scripts to run Cypress are defined in `package.json`.

## TO DO
