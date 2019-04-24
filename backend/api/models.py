from django.db import models

class Customer(models.Model):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    address = models.CharField(max_length=256)
    age = models.IntegerField()
