from django.urls import path
from articlesapp.views import ArticleView, ArticleDetailView, ArticleCreate, ArticleUpdate, CategoryView, ArticleSearch


urlpatterns = [
    path('search/', ArticleSearch.as_view(), name='search'),
    path('', ArticleView.as_view(), name = 'article_list'),
    path('', CategoryView.as_view(), name = 'article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='post_detail'),
    path('<pk>/update', ArticleUpdate.as_view(), name='update'),
    path('create', ArticleCreate.as_view(), name='create')
]
