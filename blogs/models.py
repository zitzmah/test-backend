from django.db import models

# Create your models here.
class Blog(models.Model):
    subject=models.CharField(max_length=200)
    details=models.TextField(max_length=6000)
    image_url= models.URLField(max_length=6000, blank=True, null=True, default='app.logomakr.com/3EC6KR')

