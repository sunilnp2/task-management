from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):
    """
    This model is used to store user_task of users.
    """
    objects = None
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class DifficultyKind(models.TextChoices):
        """
        Difficulty Kinds
        """

        EASY = "easy", _("Easy")
        MEDIUM = "medium", _("Medium")
        HARD = "hard", _("Hard")

    difficulty = models.CharField(
        max_length=15, choices=DifficultyKind.choices, default=DifficultyKind.EASY
    )

    class StatusKind(models.TextChoices):
        """
        Status Kind
        """

        OPEN = "open", _("Open")
        IN_PROGRESS = "progress", _("In_Progress")
        DONE = "DONE", _("Done")

    status = models.CharField(
        max_length=15, choices=StatusKind.choices, default=StatusKind.OPEN
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_by} - {self.title}'
