from django import forms
from .models import Book, Post, Profile, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# username, first_name, last_name, email, password, date


class UserForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    age = forms.DateField()


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'cover']


class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", 'email', "password1", "password2"]


class Login(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["bio", "username", "email"]