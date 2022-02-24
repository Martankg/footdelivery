from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Категория')
    def __str__(self):
        return self.title

# Create your models here.
class FoodCard(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название еды')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='core', verbose_name='Изображение')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


