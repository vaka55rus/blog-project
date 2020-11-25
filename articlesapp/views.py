from articlesapp.models import Article
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView
from .forms import CreateForm
from django.core.paginator import Paginator


class ArticleView(ListView):
    paginate_by = 2
    model = Article
    context_object_name = 'articles'
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'details'
    template_name = "article_detail.html"

class ArticleCreate(CreateView):
    form_class = CreateForm
    template_name = "create.html"

class ArticleUpdate(UpdateView):
    model = Article
    fields = [
        'title',
        'body',
        'categories',
        'published'
    ]
    template_name = "update.html"