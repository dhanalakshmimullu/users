#Installations
Python:
1.Install Python
  a.Download Python from the official website: Python.org 
  b.Verify Python installation
      python --version
      
Django:
1.Install Django
  a.Install Django using Pip 
      pip install django
  b.Verify Django installation
      django-admin --version

MySQL:
1.Install MySQL
   a.Download MySQL Community Server from the official website: MySQL Downloads
   b.Install MySQL client for Python
       pip install mysqlclient

#DataBase Setup

1.Configure database settings in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',  #Replace 'your_database_name', 'your_database_user'
        'USER': 'your_database_user',  #'your_database_password' with your MySQL database name, username, and password respectively.
        'PASSWORD': 'your_database_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

#SQL queries:
1.create database database_name
2.INSERT INTO table_name () values ()
3.show databses;
4.show tables;
5.Select * from table_name;
6.Creating table on models.

#Database Migrations:
1.Apply database migrations to create tables:
    a.Python manage.py makemigrations
    b.python manage.py migrate

Run the django Project:
1.Start the development server
   python manage.py runserver
2.Access the application in your web browser at http://127.0.0.1:8000/.

#URLs:

*Hello World:
  /hello/: Displays a simple "Hello World" message as a string.

*User Management urls:
  /user_list/: Displays a list of users
  /user/<int:user_id>/: Displays details of a specific user by their ID.
  /new_user/: Allows adding a new user.
  /user/<int:user_id>/delete/: Allows deleting a user by their ID.


