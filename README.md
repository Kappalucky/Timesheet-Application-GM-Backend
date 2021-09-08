# Timesheet-Application-GM-Backend

This folder contains the Django built backend for the Timesheet application

## Getting Started

Typically I remove all secret keys and place important information within ENV files but for this application I left everything in. I strongly recommend for you to do so if you plan on forking this repository for personal use.

#### Prerequisites

- [Python 3.0+](https://www.python.org/)
- [Pip3](https://pypi.org/project/pip/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

#### Installation

1.  Install prerequisites if you have not already
2.  Create a Virtualenv environment
```
virtualenv venv
```
3.  Activate environment
```
source venv/bin/activate
```
4.  Install requirements file from repository
```
pip3 install -r requirements.txt
```
5.  (./manage.py or Python3 manage.py) Makemigrations and migrate to Django provided SQLite database or Postgres if you have the time
```
python3 manage.py makemigrations
python3 manage.py migrate
```
6.  Create Superuser for testing on local machine (No need to if you're simply calling the api and don't care to see all the data or change it)
```
python3 manage.py createsuperuser
```
7.  Run the development server before running the frontends server. It is best to use localhost:8000. If not you will have to change the url within services/api.js of the front end main folder
```
python3 manage.py runserver
```