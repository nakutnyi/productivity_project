from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Goal, Task


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('id', 'description', 'tasks')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'description', 'subtasks')