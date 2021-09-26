from django.test import TestCase
from task_app.models import *

class MyTest(TestCase):
    index=0
    def test_1(self):
        obj_count=Task_model.objects.count()
        object=Task_model.objects.create(Title="ahmed2",State=1)
        index=object.id

        self.assertEqual(Task_model.objects.count(),obj_count+1)


    def test_2(self):
        object=Task_model.objects.create(Title="test_delet",State=1)
        count_befor=Task_model.objects.count()
        object.delete()
        count_after=Task_model.objects.count()

        self.assertEqual(count_befor,(count_after+1),"do not delete ")


