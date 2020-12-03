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
        queryset = Article.objects.filter(Q(published=True) | Q(author=self.request.user))
        return queryset


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'details'
    template_name = "article_detail.html"

    def get_queryset(self):
        queryset = Article.objects.filter(Q(published=True) | Q(author=self.request.user))
        return queryset


class ArticleCreate(CreateView):
    form_class = CreateForm
    template_name = "create.html"

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
    template_name = "update.html"


class ArticleSearch(ListView):
    model = Article
    context_object_name = 'result'
    template_name = 'search.html'

    def get_queryset(self):  # новый
        object_list = Article.objects.filter(
            title__icontains=self.request.GET['q']
        )
        return object_list
