 # PROJECT NAME
## KIDVACC

# DESCRIPTION:
# kidvacc-be-pjt-37:

 This is a site that links parents to their choice of hospital for the vaccination of their Ward/Children. The site enables parents  to be adequately informed and educated on the required vaccination to be administered to their wards/Children  based on their age range. However, a parent must be register to access the following features:
 * register their wards for vaccination
 * search , locate and choose the nearest  hospital to their location,
 * choose between  a private and a public hospital,
 * book an appointment for the vaccination of their ward from the chosen hospital,
 * make payment for the booked appointment if it is required and,
 * get a confirmation  and reminder of their booked appointment for the vaccination of their ward/children

 
This  is a project  built by the Project Team 37 , ZURI TRAINING. We are required to build a  a site and an application to solve  issues on  the vaccination of children.  Hence, tthe backend API of this site, was  built using [Django  Rest Framework]( https://www.django-rest-framework.org/) (https://www.djangoproject.com/) and  hosted on Heroku during production(https://kidvacc.herokuapp.com)



# Features/Endpoints:
- Register a  new user: (https://kidvacc.herokuapp.com/api/child/rest-auth/registration/)
- Login user   : (https://kidvacc.herokuapp.com/api/child/rest-auth/login/)
- Logout user :(https://kidvacc.herokuapp.com/api/child/rest-auth/logout/)
-password  reset: (https://kidvacc.herokuapp.com/api/child/rest-auth/password/reset/)
- book an appointment:(https://kidvacc.herokuapp.com/api/child/appointment)
- make a payment for the booked appointment:(https://kidvacc.herokuapp.com/payment/my-make)
 

  end point to the child profile : https://kidvacc.herokuapp.com/api/child/child
  parent profile : https://kidvacc.herokuapp.com/api/child/child



# Requirements:
This Project requires the following  Application and Versions:

## BASIC 
```Python  (3.5, 3.6, 3.7, 3.8 , 3.9) ```
```django   (1.11, 2.0, 2.1, 2.2, 3.0)```
```Django_Rest Framework  and other dependencies are contained in the  Requirements.txt ```


# Installation:
The backend of this site was built using a virtual enviromment(VENV).
To  create  and activate the above virtual environment to install all dependencies in this project, open your terminal and run:
```
^^^^ creating a virtual environment ^^^^
py -m venv project-name

^^^^âctivating a virtual environment ^^^^^
project name\Scripts\activate.bat

^^^^^installation of django, django rest framework and other dependencies ^^^^^^
py -m pip install the name of the application 

^^^^^Installation of applications on  a requirement.txt file ^^^^^
pip3 install -r requirements.txt (Python 3)

^^^^^updating the requirements.txt file ^^^^^
pip freeze > requirements.txt

^^^^^local command for running the server of the application ^^^^^^
python manage.py runserver
```


# Links To Design,Web Repository And Mobile Repository
- [Designs Made In Figma](https://www.figma.com/file/6GyjztMHKTzQtcFR56CSp0/Kidvacc?node-id=42%3A2)
- [Frontend Repository](https://github.com/zuri-training/kidvacc-fe-pjt-37)
- [Backend Repository](https://github.com/zuri-training/kidvacc-be-pjt-37)
- [Mobile Repository](https://github.com/zuri-training/kidvacc-mobile-pjt-37)
# NOTE
Refer to the .ENV .example file  to generate  a secret key and other variables.


### To Contribute:
Please always follow the right format in making pull request

* Fork this repository into your remote repository
* Clone the code form your remote repository into your local machine
* Create a branch with the feature name you wish to work on
* Add any changes
* Create an upstream on your local machine to pull the latest code from the develop branch of this repository
* Push to your remote branch
* Make a pull request to the develop branch of this repository

# Author:
kidvacc-be-pjt-37

# Login Credentials
create your credentials and login

## Team
# Design
- [Hawau	Morenikeji	Ahmed](https://github.com/hawauahmed)
- [Temitope	Philip	Ekundayo](https://github.com/PipEk-Nemo)
- [Monisola	Ruth	Akeredolu](https://github.com/Monnie-Ruth)
- [Rasheed	Seun	Omotayo](https://github.com/Seuntayor)
- [Mohammed	Bida	Abdullahi](https://github.com/Mbidaiii)
- [Adeniji	Muideen	Adeyemi](https://github.com/Tommie333)
- [Ayomide	Michael	Adenowo](https://github.com/Ay4realz)
# Frontend
- [Osinaya	Samson	Oluwadamilare](https://github.com/RenegadeGandhi)
- [Ezeugo	Felistus	Obieze](https://github.com/felistus)
- [Gods'Favour	Toluwalope	Omoare](https://github.com/Bebek-Hub)
- [Yusuf	Abiola	Ajaga](https://github.com/yousouph246)
# Backend
- [Elizabeth Eli](https://github.com/Duvie728)
- [Oluwadamilare	Felix	Michael](https://github.com/Michaeloluwadamilare)
- [Ruth	Ude](https://github.com/RuthJane)
- [Gabriel Adedayo	Opaleye](https://github.com/Gabriel-Zamar)
- [Ysabel	Katchy](https://github.com/MeMeee1)
- [Swaleh	Cosmas Swaleh](https://github.com/Swaleh-developer)
# Mobile
- [Samson	Achiaga](https://github.com/certified84)
- [Cephas	Oluwadamilola	Arowolo](https://github.com/CephasPeter)
# Other Contributors
- [Oluwafemi Adenuga](https://github.com/phemmylintry)




=======
Shout  out to the  Zuri team for this awesome experience.