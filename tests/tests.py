from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from user_task.models import Task


class TaskViewSetTestCase(APITestCase):
    def setUp(self):
        # Create two users
        self.user1 = User.objects.create_user(username="user1", password="password123")
        self.user2 = User.objects.create_user(username="user2", password="password456")

        self.assertEqual(self.user1.username, "user1")
        self.assertEqual(self.user2.username, "user2")

        # Create a task for user1
        self.task1 = Task.objects.create(
            title="Task 1",
            description="User1's task",
            created_by=self.user1,
            difficulty=Task.DifficultyKind.EASY,
            status=Task.StatusKind.OPEN,
        )

    def authenticate(self, user):
        """Helper method to authenticate a user."""
        self.client.force_authenticate(user=user)

    def test_create_task(self):
        """Test creating a task."""
        self.authenticate(self.user1)
        url = reverse("task-list")  # 'task-list' comes from the router's name for the viewset
        data = {
            "title": "New Task",
            "description": "New description",
            "difficulty": Task.DifficultyKind.MEDIUM,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.filter(created_by=self.user1).count(), 2)

    def test_view_own_tasks(self):
        """Test that user can view only their own tasks."""
        self.authenticate(self.user1)
        url = reverse("task-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.task1.title)

        # Ensure user2 cannot see user1's tasks
        self.authenticate(self.user2)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_update_task_status(self):
        """Test updating a task status to 'DONE'."""
        self.authenticate(self.user1)
        url = reverse("task-detail", kwargs={"pk": self.task1.pk})
        data = {"status": Task.StatusKind.DONE}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.status, Task.StatusKind.DONE)

    def test_delete_task(self):
        """Test that a user can delete only their own task."""
        self.authenticate(self.user1)
        url = reverse("task-detail", kwargs={"pk": self.task1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(pk=self.task1.pk).exists())

        # Step 2: Ensure user2 gets a 404 when trying to delete user1's new task
        new_task = Task.objects.create(
            title="User1's Task", description="Another task for user1", created_by=self.user1
        )
        self.authenticate(self.user2)
        response = self.client.delete(reverse("task-detail", kwargs={"pk": new_task.pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
