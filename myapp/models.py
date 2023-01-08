from django.db import models

# Create your models here.

class ProductModel(models.Model):
    pname = models.CharField(max_length=30)
    pprice = models.IntegerField(null=False)
    pimage = models.CharField(max_length=40)
    pdscription = models.TextField()