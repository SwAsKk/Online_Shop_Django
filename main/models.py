from django.db import models

from django.shortcuts import reverse


class Category(models.Model):
    slug = models.SlugField(
        verbose_name="Ссылка категории",
        max_length=100,
        null=False,
        blank=False,
        allow_unicode=True,
    )
    name = models.CharField(
        verbose_name="Название категории",
        max_length=100,
        null=False,
        blank=False,
    )

    image = models.ImageField(
        upload_to='static/images/caterories',
        null=True,
    )

    def __str__(self):
        return "Категория {} - {}".format(self.name, self.slug)

    class Meta:
        verbose_name = "Категория товаров"
        verbose_name_plural = "Категории товаров"


class Product(models.Model):
    image = models.ImageField(
        upload_to='media/images/products',
        null=True,
    )

    category = models.ForeignKey(
        verbose_name='Категория товара',
        to="Category",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        verbose_name='Название',
        max_length=100,
        null=False,
        blank=False,
    )

    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=6,  # До 6 цифорок
        decimal_places=2,  # Две из которых после запятой -> до 9999.99 рублей
        null=False,
        blank=False,
    )

    # TODO: Переместить в свой класс и сделать Many-To-Many или FK x2 через посредника
    compound = models.CharField(
        verbose_name='Состав',
        max_length=300,
        null=False,
        blank=False,
    )

    weight = models.IntegerField(
        verbose_name='Вес в граммах',
        null=True,
        blank=True,
    )

    def __str__(self):
        return '{} - {} / {} {} руб. {}'.format(self.id, self.type.name, self.name, self.price, self.weight)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
