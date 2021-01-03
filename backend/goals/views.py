from django.shortcuts import render
from rest_framework import viewsets
from .models import Goal, Task
from .serializers import GoalSerializer, TaskSerializer


class GoalView(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
