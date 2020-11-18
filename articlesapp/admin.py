from django.contrib import admin
from .models import Article, Category


@admin.register(Article, Category)
class ArticleAdmin(admin.ModelAdmin):
    pass


