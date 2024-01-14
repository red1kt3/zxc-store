from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.catalog.models import Product
from apps.user.models import User


class Cart(models.Model):
    product = models.ForeignKey(to=Product, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    total = models.DecimalField(verbose_name='Цена', max_digits=12, decimal_places=2, default=0)
    first_name = models.CharField(verbose_name='Имя', max_length=128)
    last_name = models.CharField(verbose_name='Фамилия', max_length=128)
    email = models.EmailField(verbose_name='E-mail')
    phone = PhoneNumberField(verbose_name='Телефон', null=True, blank=True)
    address = models.TextField(verbose_name='Адресс')
    comment = models.TextField(verbose_name='Коментарий', null=True, blank=True)

    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Время обновления', auto_now=True)


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderProduct(models.Model):
    product = models.ForeignKey(to=Product, verbose_name='Товар', on_delete=models.CASCADE)
    order = models.ForeignKey(to=Order, verbose_name='Заказ', on_delete=models.CASCADE)

    quantity = models.IntegerField(verbose_name='Количество')
    price = models.DecimalField(verbose_name='Цена', max_digits=12, decimal_places=2, default=0)


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

