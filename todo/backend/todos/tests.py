from django.test import TestCase
from .models import Todo

# Create your tests here.
class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='first todo', body='a body here')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected = f'{todo.title}'
        self.assertEqual(expected, 'first todo')
    
    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected = f'{todo.body}'
        self.assertEqual(expected, 'a body here')
    