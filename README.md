# Steps for setting up

1. Create Virtual Environments
Refer More Details: https://docs.python.org/3/library/venv.html
```
python3 -m venv venv
source venv/bin/activate
```
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
6. Admin Operations
You will be able to access the Django Admin on 127.0.0.0:8000/admin(considering you are not changing the port).
7. Non-Admin Operations
You will be able to access the Auction Application on 127.0.0.0:8000/website(considering you are not changing the port).

# Application Overview

## Home Page without Login
![home page without login](https://github.com/hiren2599/Auctions-Online/blob/master/imagesForREADME/homePageWithoutLogin.png)

## Register New User Page
![register user page](https://github.com/hiren2599/Auctions-Online/blob/master/imagesForREADME/registerNewUserPage.png)

## Login User To Auction Application
![login user page](https://github.com/hiren2599/Auctions-Online/blob/master/imagesForREADME/loginPopup.png)

## Home Page with Login
![home page with login](https://github.com/hiren2599/Auctions-Online/blob/master/imagesForREADME/homePageWithLogin.png)

## Bid Page
![bid page](https://github.com/hiren2599/Auctions-Online/blob/master/imagesForREADME/BidPage.png)

## Result Page
![result page](https://github.com/hiren2599/Auctions-Online/blob/master/imagesForREADME/resultPage.png)

## Add Balance Page
![add balance page](https://github.com/hiren2599/Auctions-Online/blob/master/imagesForREADME/addBalancePage.png)

## Login Admin User to Admin Panel
![login admin user page](https://github.com/hiren2599/Auctions-Online/blob/master/imagesForREADME/adminLoginPage.png)

##  Admin Panel Home Page
![admin panel home page](https://github.com/hiren2599/Auctions-Online/blob/master/imagesForREADME/adminOperationsPage.png)


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
