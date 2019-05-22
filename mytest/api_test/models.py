from django.db import models

# Create your models here.
# BDD - def of tables

class Customer(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return self.lastName


class Order(models.Model):
    date = models.DateField()
    refNumber = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return self.refNumber