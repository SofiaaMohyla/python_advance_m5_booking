from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ["title"]


class Room(models.Model):
    numbers = models.IntegerField(verbose_name="Номер")
    capacity = models.IntegerField(verbose_name="Місткість")
    description = models.TextField(verbose_name="Опис")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='rooms', verbose_name="Категорія")
    price = models.IntegerField(verbose_name="Ціна")
    image = models.ImageField(verbose_name="Зображення", upload_to='rooms', null=True)

    def __str__(self):
        return f'{self.numbers}'

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номери'
        ordering = ["numbers"]


# Create your models here.
class Booking(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', verbose_name="Клієнт")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings', verbose_name="Номер")

    check_in = models.DateTimeField(verbose_name="Дата заїзду")
    check_out = models.DateTimeField(verbose_name="Дата виїзду")

    phone = models.CharField(max_length=14)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} -  номер {self.room}'

    class Meta:
        verbose_name = 'Бронювання'
        verbose_name_plural = 'Бронювання'
        ordering = ["creation_time"]
