from django.db import models
import datetime
from django.utils import timezone

class Allcourses(models.Model):
    coursename=models.CharField(max_length=200)
    insname=models.CharField(max_length=100)
    startedfrom=models.DateTimeField('Started from')
    def __str__(self):
        return self.coursename

    def was_published_recently(self):
        now=timezone.now()
        return now-datetime.timedelta(days=1)<=self.startedfrom <= now


class details(models.Model):
    couse=models.ForeignKey(Allcourses, on_delete=models.CASCADE)
    ct=models.CharField(max_length=500)
    your_choice=models.BooleanField(default=False)
    def __str__(self):
        return str(self.ct)