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

# ETC
-----
* quick review for git: https://academind.com/tutorials/git-the-basics/