from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок для фото')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фоточки'
        verbose_name_plural = 'Фоточки'
        ordering = ['time_created']


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
        ordering = ['id']
