from django.db import models

# Create your models here.
class Blog(models.Model):
    subject=models.CharField(max_length=200)
    details=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='images', default='app.logomakr.com/3EC6KR')