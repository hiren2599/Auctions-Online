# Steps for setting up

1. Create Virtual Environments
Refer: https://docs.python.org/3/library/venv.html

2. Install Dependency libraries for the project
```
pip install -r requirements.txt
```
3. Make migrations
```
python manage.py makemigrations
python manage.py migrate
```
4. Create an Admin(Superuser) User
```
python manage.py createsuperuser
```
5. Final checks
```
python manage.py runserver
```

# Django Features Used

Following are the steps involved in the creation of this Django project:-

1 - Installation<br>
2 - First Steps<br>
3 - The modal layer<br>
4 - The view layer<br>
5 - The template layer<br>
6 - Forms<br>
7 - The development process<br>
8 - The admin<br>
9 - Security<br>

Sources referred<br>

* https://docs.djangoproject.com/en/1.7/howto/static-files/#configuring-static-files
* https://www.b-list.org/weblog/2006/sep/10/django-tips-laying-out-application/
* https://www.tutorialspoint.com/django/
* https://djangobook.com/
