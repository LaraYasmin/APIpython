How to Use the Project:

Create a virtual environment using the command -> python -m venv name_of_venv, then activate it -> name_of_venv/Scripts/activate
Install the requirements within the virtual environment using the following command -> pip install -r requirements.txt
My local database is named 'database', ideally, you should create a MySQL database on your local machine by editing the DATABASES section in the API settings.

Example:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '', #database name
        'USER': '', #database user
        'PASSWORD': '', #database user's password
        'HOST': '', #database host
        'PORT': '', #database port
    }
}

About the project itself:

1 - Developed using Python/Django/NinjaRestAPI
2 - Create your superuser for access to the admin
3 - To access the admin, go to /admin
4 - To access the API, go to /docs
