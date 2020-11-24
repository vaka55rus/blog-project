from articlesapp.models import Article
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView
from django.shortcuts import render
from .forms import ArticleForm
from django.shortcuts import get_object_or_404


class ArticleView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'details'
    template_name = "article_detail.html"

class ArticleCreate(CreateView):
    form_class = ArticleForm
    template_name = "create.html"



