# Generated by Django 2.2.5 on 2019-09-30 05:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('TechnicalCourses', '0006_remove_allcourses_startedfrom'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcourses',
            name='startedfrom',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 30, 5, 37, 29, 238180, tzinfo=utc), verbose_name='Started from'),
            preserve_default=False,
        ),
    ]
