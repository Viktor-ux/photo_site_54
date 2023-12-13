from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок для фото', blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации фотосъемки')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['time_created']
