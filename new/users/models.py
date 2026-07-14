from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    data = models.DateField('birthdate') 

def __str__(self):
    return self.username