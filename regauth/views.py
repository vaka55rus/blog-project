from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from regauth.forms import AuthForm, RegForm
from users.models import User


class BlogLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthForm
    success_url = reverse_lazy('article_list')

    def get_success_url(self):
        return self.success_url


class RegView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegForm
    success_url = reverse_lazy('login')


class BlogLogoutView(LogoutView):
    next_page = reverse_lazy('login')