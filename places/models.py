from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = HTMLField('Полное описание', blank=True)
    lng = models.FloatField('Широта')
    lat = models.FloatField('Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        null=True,
        blank=True,
        verbose_name='Название места',
    )
    img = models.ImageField('Изображение')
    number = models.PositiveIntegerField('Позиция', db_index=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.number} {self.place}'
