# Generated by Django 3.1.4 on 2021-01-03 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_auto_20210103_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='tasks',
            field=models.ManyToManyField(blank=True, to='goals.Task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='subtasks',
            field=models.ManyToManyField(blank=True, related_name='_task_subtasks_+', to='goals.Task'),
        ),
    ]
