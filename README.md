# [INSTAGRAM](https://instagramal.herokuapp.com/)
#### Web clone of the Instagram app
#### By **[Gabriel Gatumu](https://github.com/GabrielSpear/)**

## Description
This is a django web app clone of InstaGram whereby a user can create an account, view images, share images, like other users images and comment on them,
Users have privileges of viewing images on the homepage.

### User Stories

####  As A User I Would Like:

    Sign in to the application to start using.
    Upload my pictures to the application.
    See my profile with all my pictures.
    Follow other users and see their pictures on my timeline.
    Like a picture and leave a comment on it


## Set Up and Installations

### Prerequisites
1. Internet access
2. Python3.6
3. [Postgres](https://www.postgresql.org/download/)
4. [python virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)

### Clone the Repo

    git clone   https://github.com/GabrielSpear/InstaGrama.git

    $ cd InstaGrama

    $ pip3 install virtualenv

    $ source virtual/bin/activate

    $ python3.6 -m pip install -r requirements.txt (install all dependencies)

    $ python3.6 manage.py runserver

### Create the Database

    ```bash
    psql
    CREATE DATABASE instagram;
    ```

### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'instagram'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'
```

### Run initial Migration

```bash
python3.6 manage.py makemigrations gram
python3.6 manage.py migrate
```

### Run the app
```bash
python3.6 manage.py runserver
```
Open terminal on `localhost:8000`

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

##  Requirements

      Python3.6.4
      dj-database-url==0.4.2
      Django==1.11
      gunicorn==19.7.1
      Pillow==5.0.0
      psycopg2==2.7.4
      psycopg2-binary==2.7.4
      python-decouple==3.1
      pytz==2018.3
      whitenoise==3.3.1

## Support and contact details
```
Incase you have any questions issues while using this code do not hesitate to get in touch with me via gabrieldvjspear@gmail.com
```
### License
MIT (c) **Gabriel Gatumu**
