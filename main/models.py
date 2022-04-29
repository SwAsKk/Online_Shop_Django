from pydoc import describe
from tabnanny import verbose
from django.db import models
from django.shortcuts import reverse

class ClassicSet(models.Model):
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

    def get_absolute_url(self):
        return reverse('classic_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Классический сет'
        verbose_name_plural = 'Классические сеты'


class ComboSet(models.Model):
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

    def get_absolute_url(self):
        return reverse('combo_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Комбо сет'
        verbose_name_plural = 'Комбо сеты'

class BakedSet(models.Model):
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

    def get_absolute_url(self):
        return reverse('baked_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Запечённый сет'
        verbose_name_plural = 'Запечённые сеты'

