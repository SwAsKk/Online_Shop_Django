from os import nice
from pydoc import describe
from tabnanny import verbose
from django.db import models
from django.shortcuts import reverse

class ClassicSet(models.Model):
    image = models.ImageField(upload_to='static\images', null = True)
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

    image = models.ImageField(upload_to='static\images', null = True)
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

    image = models.ImageField(upload_to='static\images', null = True)
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

  #  def get_absolute_url(self):
   #     return reverse('baked_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Запечённый сет'
        verbose_name_plural = 'Запечённые сеты'


class Sushi(models.Model):

    image = models.ImageField(upload_to='static\images', null = True)
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

    #def get_absolute_url(self):
    #   return reverse('sushi_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Суши'
        verbose_name_plural = 'Суши'


class Rolls(models.Model):

    image = models.ImageField(upload_to='static\images', null = True)
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

    #def get_absolute_url(self):
     #   return reverse('rolls_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Роллы'
        verbose_name_plural = 'Роллы'


class Wok(models.Model):

    image = models.ImageField(upload_to='static\images', null = True)
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
        return reverse('wok_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Вок'
        verbose_name_plural = 'Вок'


class Pizza(models.Model):

    image = models.ImageField(upload_to='static\images', null = True)
    name = models.CharField(
        verbose_name='Название',
        max_length= 30,
        null= False,
        blank = False,
    )

    price = models.IntegerField(
        verbose_name= 'Цена маленькая пицца',
        null= False,
        blank = False,
    )
    priceS = models.IntegerField(
        verbose_name='Цена маленькой пиццы',
        default=100,
        null=False,
        blank=False
    )
    priceM =models.IntegerField(
        verbose_name='Цена средней пиццы',
        default=100,

        null=False,
        blank=False,
    )

    priceL = models.IntegerField(
        verbose_name='Цена большой пиццы',
        default=100,
        null=False,
        blank=False,
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
        return reverse('pizza_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight,self.priceS,self.priceM,self.priceL)

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пицца'


class BakedSets(models.Model):

    image = models.ImageField(upload_to='static\images', null = True)
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
        return reverse('bakedroll_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Запечённый ролл'
        verbose_name_plural = 'Запечённые роллы'


class Sets(models.Model):

    image = models.ImageField(upload_to='static\images', null = True)
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
        return reverse('set_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Набор'
        verbose_name_plural = 'Наборы'


class Tempured(models.Model):

    image = models.ImageField(upload_to='static\images', null = True)
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
        return reverse('tempured_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Темпур'
        verbose_name_plural = 'Темпура'



class Soup(models.Model):

    image = models.ImageField(upload_to='static\images', null = True)
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
        return reverse('soup_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Суп'
        verbose_name_plural = 'Супы'


class HotAndSalads(models.Model):

    image = models.ImageField(upload_to='static\images', null = True)
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
        return reverse('hot_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Горячее и салаты'
        verbose_name_plural = 'Горячее и салаты'


class MiniRolls(models.Model):

    image = models.ImageField(upload_to='static\images', null = True)
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
        return reverse('mini_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Мини ролл'
        verbose_name_plural = 'Мини роллы'


class MagRolls(models.Model):
    
    image = models.ImageField(upload_to='static\images', null = True)
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

    #def get_absolute_url(self):
      #  return reverse('mag_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Маг ролл'
        verbose_name_plural = 'Маг роллы'

class Vegan(models.Model):

    image = models.ImageField(upload_to='static\images', null = True)
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
        return reverse('vegan_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Вег меню'
        verbose_name_plural = 'Вег меню'

class Deserts(models.Model):

    image = models.ImageField(upload_to='static\images', null = True)
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
        return reverse('deserts_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Десерт'
        verbose_name_plural = 'Десерты'


class Drinks(models.Model):

    image = models.ImageField(upload_to='static\images', null = True)
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
        return reverse('drink_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Напиток'
        verbose_name_plural = 'Напитки'

class SushiStuff(models.Model):

    image = models.ImageField(upload_to='static\images', null = True)
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
        return reverse('stuff_details_url', kwargs = {'id': self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.price, self.compound, self.weight)

    class Meta:
        verbose_name = 'Все для суши'
        verbose_name_plural = 'Все для суши'






















