# Generated by Django 2.2.5 on 2019-09-30 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TechnicalCourses', '0004_auto_20190930_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allcourses',
            name='startedfrom',
            field=models.DateTimeField(verbose_name='Started from'),
        ),
    ]