from django.db import models


class User(models.Model):
    Name = models
    phone_number = models.IntegerField(unique=True)
    stock_label = models.CharField()

# Create your models here.
