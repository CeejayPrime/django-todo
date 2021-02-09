# Generated by Django 3.0 on 2021-02-06 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subtitle', models.CharField(max_length=20)),
                ('completed', models.BooleanField(default=False)),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
