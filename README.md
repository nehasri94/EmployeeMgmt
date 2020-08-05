# EmployeeMgmt
Employee data management using Django
About the Project:

Implement a user management system with basic authentication.
Each User object should have basic information like

User Name
Password
Role
First name
Last name
Email
Phone number
Employee id
Address
Pin code

Have a default user ‘admin’ with password as ‘admin’
REST server should be implemented to support all  CRUD operations with basic authentication
In Backend – User objects can be stored in DB/File to persist.     
Use cases expected to cover using rest client(we can use browser tools for this):

Create a new/existing user             
Delete an existing/non existing user
Update an existing/non existing user
Get an existing/non existing user with given name/email/phone number
Get all users from system

Required Software and Installation:

1. python 3.4.2
2. django-admin 2.0
3. pip 18.1
4. easy_install (setuptools 2.1)
5. Pycharm Community Edition 2018.1.1

Commands for installing different frameworks and libraries:

1. pip install django==2.0 : for insatlling Django Framework.
2. django-admin startproject Project_Name : for creating a Django Project.
3. python manage.py runserver : for starting the development server (localhost) that comes along with Django.
4. python mamage.py startapp App_Name : for creating an application in Django (App_Name should be replaced by the name of the application (employee)).
5. python manage.py makemigrations App_Name : for synchronization of code with the database (SQLite database is used by the django framework by default).
6. python manage.py migrate : to sync all the modifications done in code with the database (models.py modifications).
7. python mamage.py sqlmigrate App_name 0001 : to check whether tables are created in the database or not (id = 0001 is the id which is generated when we run the 5th command).
8. python manage.py createsuperuser : to create the superuser by giving username , email and password. Using the credentials the user can login into the website powered by Django framework (Admin Interface).
9. pip install djangorestframework : for installing the django rest framework (creating a simple REST API for performing the CRUD Operations).

Note : Please use these credentials to login : 

Username : pass
Password : pass@4567
email : pass@gmail.com (not required during login)

Instructions for running the Employee Management System:

1. In the Pycharm terminal, start the server using the 3rd command listed above. This will generate a URL (https://127.0.0.1:8080/) , open this URL in a browser.
2. This will show the default page of a django powered website.
3. Now visit this URL : https://127.0.0.1:8080/admin/ - This will redirect to the Login page where the login credentials need to be entered.
4. Once login is completed, the user can see the records inserted into the database and can manage the modifications and deletion of any record from website itself.
5. Now visit the URL :  https://127.0.0.1:8080/employee/ - This will redirect the user to main application (employee) where the REST API is implemented to perform the create , write , delete and update operations.
6. The webpage visited in step 5 contains a REST API endpoint URL, clicking this URL will redirect to another webpage that displays the records of the database in parsed JSON format. This webpage also contains an HTML form with all 
the required fields , using this the user can insert a new record in the database by clicking on the POST button.




