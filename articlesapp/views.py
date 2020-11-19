from articlesapp.models import Article
from django.views.generic import ListView
from django.views.generic import DetailView

class ArticleView(ListView):
    model = Article
    context_object_name = 'articles_object'
    template_name = "about.html"

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'details'
    template_name = 'details.html'