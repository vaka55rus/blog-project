from .models import Article
from django.forms import ModelForm, TextInput


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'categories', 'published']
