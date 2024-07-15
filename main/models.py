from django.db import models


class User(models.Model):
    name = models.CharField(max_length=35,verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')