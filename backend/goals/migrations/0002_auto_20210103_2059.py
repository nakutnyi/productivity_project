# Generated by Django 3.1.4 on 2021-01-03 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='tasks',
            field=models.ManyToManyField(null=True, to='goals.Task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='subtasks',
            field=models.ManyToManyField(null=True, related_name='_task_subtasks_+', to='goals.Task'),
        ),
    ]
