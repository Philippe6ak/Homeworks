from django.db import models


# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Customer(models.Model):
    comp_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)


class Products(models.Model):
    prod_name = models.CharField(max_length=30)
    price = models.BigIntegerField()


class OrderDetails(models.Model):
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
