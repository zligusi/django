from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    data = models.DateField('birthdate', null=True, blank=True)

    def __str__(self):
     return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'