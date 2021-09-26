from django.urls import reverse
import unittest
from task_app.models import *
from task_app.serializers import *


class BaseModelTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()
        cls.author= Task_model(Title="Ahmed",State=1)
        cls.author.save()


class Task_model_Title(BaseModelTestCase):

    def test_created_properly(self):
        self.assertEqual(self.author.Title, 'Ahmed')
        self.assertEqual(self.author.State, 1)


