# Generated by Django 2.2.5 on 2019-09-30 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TechnicalCourses', '0007_allcourses_startedfrom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allcourses',
            name='startedfrom',
        ),
    ]
