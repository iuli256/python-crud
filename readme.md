# Django CRUD App

This is application is the test:

- Implement CRUD using CBV (Class Based Views).
- Implement CRUD using FBV (Function Based Views).

## Install docker container with postgresql database
In the root of the project there are 2 files: database.env and docker-compose.yml
In database.env you can set user, password and database that have to be on server
In docker-compose.yml you can set a different port for server. I've used 5433 to 
be different from the standard one in order to avoid any conflicts with existing
instalations on the system.

To start the container with postgres you need to have installed locally on your machine 
docker and docker-compose. In the root folder of the project run the following command
    
    docker-compose -f docker-compose.yml up
    
if everything went good you should see: database system is ready to accept connections


## Install Required Packages

The Django project dependency can be installed by use the following command:

    pip install -r requirements.txt

Django 2 requires Python 3, if you need help setting up Python 3 on your machine you can consult
DigitalOcean great documentation on 
[How To Install and Set Up a Local Programming Environment for Python 3](https://www.digitalocean.com/community/tutorial_series/how-to-install-and-set-up-a-local-programming-environment-for-python-3)

## Running the Application

Before running the application we need to create the needed DB tables:

    ./manage.py migrate

Now you have to create first user in order to be able to login on the application:

    ./manage.py createsuperuser
    
Finally you can run the development web server:

    ./manage.py runserver

To access the applications go to the URL <http://localhost:8000/>
