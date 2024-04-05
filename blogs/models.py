from django.db import models

# Create your models here.
class Blog(models.Model):
    subject=models.CharField(max_length=200)
    details=models.CharField(max_length=1000)
    image=models.CharField(max_length=1000, blank=True, null=True default='app.logomakr.com/3EC6KR')