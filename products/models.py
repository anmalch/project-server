from django.db import models

# модели= таблицы в БД
# madels.py - файл, отвечающий за хранение таблиц для БД

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True) #данное поле может быть и пустым, тк blank=True, null=True

class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.CharField(max_length=64, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity=models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE) #каскадное удаление
