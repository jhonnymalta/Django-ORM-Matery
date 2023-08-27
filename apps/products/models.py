from django.db import models
from datetime import datetime


class Fabricant(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        ordering = ["country"]

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length= 100)
    price = models.DecimalField(max_digits=5,decimal_places=2,blank=True)
    qtd = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    url = models.SlugField()
    is_active = models.BooleanField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    fabricant = models.OneToOneField(Fabricant,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
