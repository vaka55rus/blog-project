from articlesapp.models import Article, Category
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView
from .forms import CreateForm
from django.db.models import Q
from django_filters.views import FilterView
from .filters import ArticleFilter


class ArticleView(ListView):
    paginate_by = 5
    model = Article
    context_object_name = 'articles'
    template_name = 'article_list.html'

    def get_queryset(self):
        queryset = Article.objects.filter(Q(published=True) | Q(author=self.request.user))
        return queryset


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'details'
    template_name = 'article_detail.html'

    def get_queryset(self):
        queryset = Article.objects.filter(Q(published=True) | Q(author=self.request.user))
        return queryset


class ArticleCreate(CreateView):
    form_class = CreateForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleCreate, self).form_valid(form)


class ArticleUpdate(UpdateView):
    model = Article
    fields = [
        'title',
        'body',
        'categories',
        'published'
    ]
    template_name = 'update.html'


class ArticleFilterView(FilterView):
    filterset_class = ArticleFilter
    context_object_name = 'filter'
    template_name = 'search_filter.html'