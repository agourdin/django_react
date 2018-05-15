from django.test import TestCase
from .models import ModelExample


class ModelExampleTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        ModelExample.objects.create(title='first title')
        ModelExample.objects.create(description='a description here')

    def test_title_content(self):
        model_example = ModelExample.objects.get(id=1)
        expected_object_title = f'{model_example.title}'
        self.assertEquals(expected_object_title, 'first title')

    def test_description_content(self):
        model_example = ModelExample.objects.get(id=2)
        expected_object_description = f'{model_example.description}'
        self.assertEquals(expected_object_description, 'a description here')
