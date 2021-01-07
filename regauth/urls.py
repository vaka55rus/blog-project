from django.urls import path
from regauth.views import BlogLoginView, RegView, BlogLogoutView

urlpatterns = [
    path('', BlogLoginView.as_view(), name='login'),
    path('register', RegView.as_view(), name='register'),
    path('logout', BlogLogoutView.as_view(), name='logout'),
]