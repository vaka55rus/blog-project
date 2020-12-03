from .models import Article
from django.forms import ModelForm


class CreateForm(ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'body',
            'categories',
            'published'
        ]