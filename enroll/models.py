from django.db import models

# Create your models here.
class UserForm(models.Model):
    Url = models.CharField(max_length=100)
    IP = models.IntegerField()
    requestHeaders = models.EmailField()