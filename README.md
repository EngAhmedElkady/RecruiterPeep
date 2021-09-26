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
````
HTTP 200 OK
Allow: POST, OPTIONS, GET
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "Title": "ahmed",
        "State": 1
    }
]
````
* updat data: 
if you try to update state form 1 to  3
will raise ValidationError

````
HTTP 400 Bad Request
Allow: PUT, DELETE, OPTIONS, GET
Content-Type: application/json
Vary: Accept

{
    "State": [
        "draft → active → done → archived.you can not move from draft to done,can not move from active or done to draft,and can notmove from archived backward."
    ]
}
````
because validate_State in serializers.py
````
 def validate_State(self,value):
        try:
            stat1=self.instance.State
        except:
            return value
            
        if 0 <= (value- stat1) <= 1 or value == 4:
              return value
        else:
            raise serializers.ValidationError("draft → active → done → archived.you can not move from draft to done,can not move from active or done to draft,and can notmove from archived backward.")
````

# test
* test models
* test views
* test database

````
class BaseModelTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()
        cls.author= Task_model(Title="Ahmed",State=1)
        cls.author.save()
````

````
(task_state_api) E:\django\RecruiterPeep\task_state_api>python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.022s

OK
Destroying test database for alias 'default'...

(task_state_api) E:\django\RecruiterPeep\task_state_api>

````

by the update function in Task_app.models

````
    def update(self,*args,**kwargs):
        new_state= kwargs.pop('State', False)
        if validate_gender(new_state,self.State):
            self.State=new_state
        super(Task_model, self).save(*args, **kwargs)  
        return True

````


# Technical problem:
## idea:
* sort the array.   o(nlog)
* find the minimum absolute difference between two adjacent elements in the array. o(n)

time : o(nlogn)
space: o(n)

