from django.db import models
from django.urls import reverse


class Status(models.IntegerChoices):
    """Модель перечисляемого поля."""
    AVAILABLE = 1, 'Доступен'
    RENTED = 0, 'Недоступен'


class Helicopter(models.Model):
    """Модель вертолета."""
    name = models.CharField(max_length=50, verbose_name="Название")
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(verbose_name="Описание")
    passenger_capacity = models.IntegerField(verbose_name="Вместимость пассажиров")
    range = models.IntegerField(verbose_name="Дальность полета, км")
    speed = models.IntegerField(verbose_name="Максимальная скорость, км/с")
    rent_price = models.IntegerField(verbose_name="Стоимость аренды, 1 час")
    status = models.IntegerField(choices=Status.choices, default=Status.AVAILABLE, verbose_name="Статус")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вертолет"
        verbose_name_plural = "Вертолеты"
        ordering = ['id']
        indexes = [
            models.Index(fields=['name'])
        ]

    def get_absolute_url(self):
        return reverse('st_id', kwargs={'st_id': self.id})  # абсолютный URL объекта


class Applications(models.Model):
    """Модель заявки."""
    full_name = models.CharField(max_length=50, verbose_name="ФИО")
    number_phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(max_length=50, verbose_name="Электронная почта")
    number_of_passengers = models.IntegerField(verbose_name="Количество пассажиров")
    date_create = models.DateTimeField(auto_now_add=True)
    helicopter = models.ForeignKey(Helicopter, on_delete=models.CASCADE, related_name='applications', verbose_name='Вертолет')

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['date_create']