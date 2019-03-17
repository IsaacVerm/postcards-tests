#!/bin/bash

# create Python 3 virtual environment
virtualenv -p python3 venv

# activate the environment
source venv/bin/activate

# install required packages
pip install -r requirements.txt

# get the latest version of the postman tests
python export_postman_collection.py