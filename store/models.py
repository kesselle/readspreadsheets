from django.db import models

# Create your models here.

class Product(models.Model):
    item=models.CharField(max_length=255)
    quantity=models.PositiveBigIntegerField()
    amount=models.DecimalField(max_digits=9 ,decimal_places=2) 
    date=models.DateField()