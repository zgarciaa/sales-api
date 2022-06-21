# Store API

This store API provides the following functionality:
- Manage sales
- Manage products
- Manage users
- Make daily closings
- Make a monthly balance

# Inside API folder

- cd API

## Create a virtual environment

- python -m venv env

- env\Scripts\activate


## Install the requierements

- pip install -r requirements.txt


## Create database migration

- python manage.py makemigrations


## Applying migrations

- python manage.py migrate


## Run the project

- python manage.py runserver

- Go to http://localhost:8000/
