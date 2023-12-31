# Python-Django
----------------
* Django are built do the lastest version of Pyhton 3.x
    - Batteries included (there are lots things are already built-in in django project)
    - Django is good for a big scale python project.
    - For light weight can used a flask Framework

* instaling Django : (https://www.djangoproject.com/download/)
```console
$ pip3 install Django
//try
$ django-admin
```
* Starting Django project:
```console
$ django-admin startproject [-h] [--template TEMPLATE]
                                 [--extension EXTENSIONS] [--name FILES]
                                 [--exclude [EXCLUDE]] [--version]
                                 [-v {0,1,2,3}] [--settings SETTINGS]
                                 [--pythonpath PYTHONPATH] [--traceback]
                                 [--no-color] [--force-color]
                                 name [directory]

positional arguments:
  name                  Name of the application or project.
  directory             Optional destination directory

```
* starting a django apps:
```
$ python manage.py startapp your_apps_name
```
* all basic documentation:(https://docs.djangoproject.com/en/4.2/intro/tutorial01/)

* Virtual enviroment in python
    1. Installing virtualenv
        - Note If you are using Python 3.3 or newer, the venv module is the preferred way to create and manage virtual environments. venv is included in the Python standard library and requires no additional installation. If you are using venv, you may skip this section.
        - virtualenv is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. You can install virtualenv using pip.
        ```console
        $ py -m pip install --user virtualenv
        ```
    2. Creating a virtual environment
        - venv (for Python 3) and virtualenv (for Python 2) allow you to manage separate package installations for different projects. They essentially allow you to create a “virtual” isolated Python installation and install packages into that virtual installation. When you switch projects, you can simply create a new virtual environment and not have to worry about breaking the packages installed in the other environments. It is always recommended to use a virtual environment while developing Python applications.
    3. There are many way to active python env: (it will show =>> (env) )
        * On Windows using the Command Prompt: path\to\venv\Scripts\activate.bat
        * On Windows using PowerShell: path\to\venv\Scripts\Activate.ps1
        * On Windows using Git Bash : "$ . Activate"
        * for exit just using "deactivate" then (env) will gone

* Build in Django development server using
```console
$ py manage.py runserver
// it'will running on http://127.0.0.1:8000/
// and cmd will tailing logs django server
```

* Starting building apps on Django project structure:
```console
$ ./manage.py startapp your_apps_name
// your_apps_name will created automated inside Django project structure.
```
* Diffrent "Project" and "apps" in Django:
    - Project hold configuration settings for website and many "apps" serve as module code/feature.
    - apps serving as module / feature in our project helping encapsulate code better.
    - in this repo project are "myDjangoProject" and other are apps

* build in django app structure:
    1. migration: for database migration.
    2. __init__ : to indicate folder as module.
    3. admin    : Django admin.
    4. apps     : as identifier django
    5. models   : for database models
    5. test     : for unit testing
    5. view     : all about view.

* adding templates in Django can be automated by listing our name apps in apps settings.py
* DTL (Django Template Language) is special language to render template used by Django:
    - Documentation to tags (https://docs.djangoproject.com/en/4.2/ref/templates/builtins/)
* Creating super admin for djanog admin moduiles:
```
$ py3 manage.py createsuperuser
```
* each project can listing a model to manages in admin panel using admin.py
* full documentation in django-admin (https://docs.djangoproject.com/en/4.2/ref/contrib/admin/) 
# Django models
---------------

* Inside of django apps there is a django models.py that will hold models that used for specifict apps. 
* after defining some models django can automate make migration and migrate it using
* Circular Relations & lazy Relations:
    - Sometimes, you might have two models that depend on each other - i.e. you end up with a circular relationship. Or you have a model that has a relation with itself.Or you have a model that should have a relation with some built-in model (i.e. built into Django) or a model defined in another application.
    - doc about it .(https://docs.djangoproject.com/en/3.2/ref/models/fields/#module-django.db.models.fields.related) 
```
# To make migration file
$ py ./myDjangoProject/manage.py makemigrations
# to execute migration file
$ py ./myDjangoProject/manage.py migrate
```
* Django queerying is chached within query set statement.
* Deleting models:
    - https://docs.djangoproject.com/en/3.1/topics/db/queries/#deleting-objects
* Updateing models (bulk update):
    - https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-update
* creating models (bulk create):
    - https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-create
* converting id in url model using slug
* Django have a wrapper class based to handle incoming post/get in Django (https://docs.djangoproject.com/en/4.2/topics/class-based-views/).

# Deploymnt in Django framework
-------------------------------
* full documentation  : https://docs.djangoproject.com/en/4.2/howto/deployment/
* Django currently supports two interfaces: WSGI and ASGI.
    - WSGI is the main Python standard for communicating between web servers and applications, but it only supports synchronous code.
    - ASGI is the new, asynchronous-friendly standard that will allow your Django site to use asynchronous Python features, and asynchronous Django features as they are developed.

* few serving static file in django :
    1. configuring django files (urls.py).
    2. To configure webapps to server separate from django.
    3. Use dedicated server to serve only static files.

* best practice to separate static file of our code and user upload in separate folder. (configure in setting.py)
```
# command to collecting(copying) all static file in our apps to single folder 
$ py manage.py collectstatic
```
* Adding static url to server by django in url.py by code in the end of dictionary:
```
    +static(settings.STATIC_URL, document_root=settings.STATIC_URL)
```
* Setting depedency lib for django and webserver:
```
$ py -m pip freeze > requirement.txt
```
* Creating virtual enviroment for specified project:
```
$ py -m venv django_your_enviroment_project_name
```
* Using enviroment variable for some setting.py (from os import getenv)
* deploying to AWS beanstalk
    - .ebextenxsion/django.config needed for elastic beanstalk deploy
    - zipping all folder code nedeed for deploy.
    - dont forget to filling environment property in hosting server.

* static-files.config used for set webserver to serve static file diffrent from django apps.
* serving static file using AWS S3 are specify webserver to server files.
    - view module to attact out project to automated uploading to AWS s3(using AWS IAM)
    ```
    # django-storages are django modules for managing local storage
    $ pip install django-storages
    # boto3 AWS modules 
    $ pip install boto3
    ```
    - adding "storages" in django apps.
    - add AWS S3 variable in setting.py:
        - AWS_STORAGE_BUCKET_NAME
        - AWS_S3_REGION_NAME
        - AWS_ACCESS_KEY_ID
        - AWS_SECRET_aCCESS_KEY
        - AWS_S3_COSTUME_DOMAIN
        - STATICFILES_STORAGE
    - managing separate static upload file using costume_storage.py & some variable:
        - STATICFILES_FOLDER = "static"
        - MEDIAFILES_FOLDER = "media"
        - STATICFILES_STORAGE = "custom_storages.StaticFileStorage"
    - run "py manage.py collectstatic" then all static file will endup uploading in AWS S3 server.
    
# Setting database
-----------------
* full database documentation for django (https://docs.djangoproject.com/en/4.2/ref/databases/)
    - for postgrest using psycopg2-binary
    ```
    $ pip install psycopg2-binary

    ```

# ETC
-----
* quick review for git: https://academind.com/tutorials/git-the-basics/
* Django extendsion for vs code:
    Name: Django
    Id: batisteo.vscode-django
    Description: Beautiful syntax and scoped snippets for perfectionists with deadlines
    Publisher: Baptiste Darthenay