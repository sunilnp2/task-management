from django.contrib.auth.models import User
from rest_framework import serializers

from user_task.models import Task


class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class TaskSerializer(serializers.ModelSerializer):
    created_by = UsernameSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'created_by', 'difficulty', 'status', 'created_at', 'updated_at')
        # read_only_fields = ('created_by',)
