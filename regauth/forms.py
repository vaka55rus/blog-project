from django.contrib.auth.forms import AuthenticationForm

from articlesapp import forms
from users.models import User


class AuthForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]


class RegForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user