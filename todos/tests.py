from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(title="The title", body="The body")

    def test_model_content(self):
        self.assertEqual(self.todo.title, "The title")
        self.assertEqual(self.todo.body, "The body")
        self.assertEqual(str(self.todo), "The title")

    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}), format="json"
        )
