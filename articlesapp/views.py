from articlesapp.models import Article, Category
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView
from .forms import CreateForm
from django.db.models import Q


class CategoryView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = "article_list.html"

class ArticleView(ListView):
    paginate_by = 5
    model = Article
    context_object_name = 'articles'
    template_name = "article_list.html"

    def get_queryset(self):
        queryset = Article.objects.filter(published__exact = 'True')
        return queryset

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