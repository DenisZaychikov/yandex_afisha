from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название экскурсии')
    short_description = models.TextField(blank=True,
                                         verbose_name='Короткое описание')
    long_description = HTMLField(blank=True, verbose_name='Длинное описание')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE,
                              verbose_name='Название экскурсии',
                              related_name='images')
    image = models.ImageField(verbose_name='Название картинки')
    my_order = models.PositiveIntegerField(default=0, verbose_name='Позиция',
                                           db_index=True)

    class Meta(object):
        ordering = ['my_order']

    def __str__(self):
        return f'{self.place}'
