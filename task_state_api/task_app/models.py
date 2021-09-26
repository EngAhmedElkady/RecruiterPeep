from django.urls import reverse
from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError

# Create your models here.

def validate_gender(value,stat1):
                
        if 0 <= (value- stat1) <= 1 or value == 4:
                return value
        else:
            raise ValidationError("draft → active → done → archived.you can not move from draft to done,can not move from active or done to draft,and can notmove from archived backward.")

class Task_model(models.Model):

   
    types=(
        (1,"draft"),
        (2,"active"),
        (3,"done"),
        (4,"archived"),
    )
   
    Title=models.CharField(max_length=255)
    State=models.IntegerField(choices=types)    


    def update(self,*args,**kwargs):
        new_state= kwargs.pop('State', False)
        if validate_gender(new_state,self.State):
            self.State=new_state
        super(Task_model, self).save(*args, **kwargs)  
        return True

   

    def __str__(self):
        return self.Title
    
    