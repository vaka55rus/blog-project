from django.urls import path
from articlesapp.views import ArticleView, ArticleDetailView, ArticleCreate
from . import views

# from articlesapp.forms import ArticleForm

urlpatterns = [
    path('', ArticleView.as_view(), name = 'article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='post_detail'),
    #path('create', views.create, name='create'),
    path('create', ArticleCreate.as_view(), name='create')
]
