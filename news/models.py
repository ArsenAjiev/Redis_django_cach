from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='опубликовано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Возвращает url-адрес для доступа к определенной новости.
        return reverse('news_detail', kwargs={'news_pk': self.pk})
