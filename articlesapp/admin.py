from django.contrib import admin
from .models import Article
from .models import Author
from .models import Category


admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Category)
