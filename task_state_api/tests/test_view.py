from django.urls import reverse
import unittest
from task_app.models import *



class BaseModelTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()
        cls.author= Task_model(Title="Ahmed",State=1)
        cls.author.save()

class Task_model_State(BaseModelTestCase):


    def test_update_State1(self):
        new_state=2
        self.assertGreaterEqual(new_state,1,"outside the range")
        self.assertLessEqual(new_state,4,"outside the range")
        self.assertTrue(self.author.update(State=new_state))
        # print(self.author.State)

    

    def test_update_State2(self):
        new_state=4
        self.assertGreaterEqual(new_state,1,"outside the range")
        self.assertLessEqual(new_state,4,"outside the range")
        self.assertTrue(self.author.update(State=new_state))
        # print(self.author.State)

    



