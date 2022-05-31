from os import nice
from pydoc import describe
from tabnanny import verbose
from django.db import models
from django.forms import CharField, ImageField
from django.shortcuts import reverse


class Product(models.Model):
    id = models.AutoField(
        primary_key=True,

    )
    image = models.ImageField(upload_to='static\images', null = True)

    #Type choise
    CHOICES=(
        ('Суши', 'Суши'),
        ('Роллы','Роллы'),
        ('Запечённые роллы','Запечённые роллы'),
        ('Наборы','Наборы'),
        ('Темпура','Темпура'),
        ('Лапша wok','Лапша wok'),
        ('Супы','Супы'),
        ('Горячее и салаты','Горячее и салаты'),
        ('Мини роллы','Мини роллы'),
        ('Маг роллы','Маг роллы'),
        ('Вегетарианское меню','Вегетарианское меню'),
        ('Десерты','Десерты'),
        ('Напитки','Напитки'),
        ('Всё для суши','Всё для суши'),
        ('Пицца','Пицца'),
    )
    type = models.CharField(
        verbose_name='Тип товара',
        max_length=40,
        choices = CHOICES,
        null=False,
        blank=False,
    )

    name = models.CharField(
        verbose_name='Название',
        max_length= 30,
        null= False,
        blank = False,
    )

    price = models.IntegerField(
        verbose_name= 'Цена',
        null= False,
        blank = False,
    )

    compound = models.CharField(
        verbose_name= 'Состав',
        null = False,
        blank = False,
        max_length= 200,
    )

    weight = models.IntegerField(
        verbose_name= 'Вес',
        null= False,
        blank = False,
    )

   # def get_absolute_url(self):
     #   return reverse('product_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id,self.image,self.type, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'





















