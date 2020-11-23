from django.urls import path
from articlesapp.views import ArticleView, ArticleDetailView

# from articlesapp.forms import ArticleForm

urlpatterns = [
    path('', ArticleView.as_view()),
    path('<int:pk>/', ArticleDetailView.as_view(), name='post_detail'),
    # path('articlesadd/', ArticleForm()),
]
