from django.db import models
from django.urls import reverse

class Category(models.Model):
    category = models.CharField(max_length=300, verbose_name='Имя категории')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='Заголовок статьи')
    body = models.TextField(verbose_name='Содержание статьи')
    categories = models.ManyToManyField(Category, verbose_name='Категории статьи')
    date_create = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False, verbose_name='Опубликовать')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'