from django.db import models


class Task(models.Model):
    """Tasks describe what a person should accomplish to achieve goal(s)"""

    description = models.TextField(blank=False, null=False, max_length=200)
    subtasks = models.ManyToManyField('self', blank=True)

    def __str__(self) -> str:
        return self.description

class Goal(models.Model):
    """
    Goals are a central point of the whole application.

    The idea is to make computations and determine the best combination
    of tasks that help accomplish particular goal with minimum effort/time.
    """

    description = models.TextField(blank=False, null=False, max_length=200)
    tasks = models.ManyToManyField(Task, blank=True)  # many ways to achieve

    def __str__(self) -> str:
        return self.description