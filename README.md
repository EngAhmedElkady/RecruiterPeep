# Technical Project
An API is needed that changes the task status based on a predefined state machine that this task
must respect.
So the workflow of the task: draft → active → done → archived. 

## Overview
* Fully working API
* Well-structured and readable code
* Instructions in the README on how to run the project.
* Writing unit tests

## Technologies
* asgiref==3.4.1
* Django==3.2.7
* django-filter==21.1
* djangorestframework==3.12.4
* Markdown==3.3.4
* pytz==2021.1
* sqlparse==0.4.2

## Usage
first runserver
````
python manage.py runserver
````
in Task_app.urls
````
from django.urls import path,include
from . import views

urlpatterns = [
    path('api/data/', views.Data_list), 
    path('api/data/<int:pk>', views.Data_detail,name="data_details"),

]

````
* get all data
````
http://127.0.0.1:8000/api/data/

````
* get data with id 1
````
http://127.0.0.1:8000/api/data/1
````


