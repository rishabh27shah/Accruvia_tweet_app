# Tweet application.

## Steps to install and run server

### Create and Activate Virtual Environment
* Run `$ python3 -m venv env` command to create virtual environment
* Run `$ source env/bin/activate` command to activate virtual environment

### Update value in .env file
* Run `$ source .env` command to activate environment variables

### Install requirements
* Run `$ pip3 install -r requirements.txt` command to Install project requirement

### Migrate and Run Server
* Run `$ python manage.py migrate` command to apply migrations on your local.
* Run `$ python manage.py runserver 8000` command to run project on your local machine