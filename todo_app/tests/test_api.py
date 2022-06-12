from rest_framework.test import APITestCase

from django.urls import reverse

from todo_app.models import ToDoList


class TodoAppTestCase(APITestCase):
    def test_get(self):
        list_1 = ToDoList.objects.create(title='example list')
        url = reverse('list-add')
        print(url)
        response = self.client.get(url)
        for i in response:
            print(i)
        print(response)
