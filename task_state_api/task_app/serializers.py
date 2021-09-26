from rest_framework import serializers
from .models import *
# Serializers define the API representation.

class Task_modelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_model
        fields ='__all__'


    def validate_State(self,value):
        try:
            stat1=self.instance.State
        except:
            return value
            
        if 0 <= (value- stat1) <= 1 or value == 4:
              return value
        else:
            raise serializers.ValidationError("draft → active → done → archived.you can not move from draft to done,can not move from active or done to draft,and can notmove from archived backward.")

    def update(self,instance,validated_data):
        instance.Title=validated_data.get('Title',instance.Title)
        instance.State=validated_data.get('State',instance.State)
        instance.save()
        return instance

   
   