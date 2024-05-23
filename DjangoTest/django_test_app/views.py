from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookForm, UserForm, Registration, Login, PostForm, ProfileForm
from .models import Post, Comment, Profile, User
from django.contrib.auth import authenticate, login, logout
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import  JsonResponse
from django.template.loader import render_to_string
from django.views.generic.detail import DetailView


class HomePage(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'post'


class RegistrationPage(CreateView):
    template_name = 'registration.html'
    # fields = ['username', ]
    # model = User
    form_class = Registration
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class PostPage(DetailView):
    template_name = 'post.html'
    model = Post
    slug_field = 'id'
    context_object_name = "post"

    def get_success_url(self):
        return f'/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(id=self.kwargs['pk'])
        context['comment'] = Comment.objects.filter(post=Post.objects.get(id=self.kwargs['pk']))
        return context

    def post(self, request, *args, **kwargs):
        data = self.request.POST
        comment = Comment(text=data['text'], post=self.object, user=self.request.user)
        comment.save()
        response = render_to_string("partical/comment.html", {'comment': comment})
        return JsonResponse(response, safe=False)


class PostCreate(CreateView):
    form_class = PostForm
    template_name = 'postcreate.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/login')


class LoginPage(LoginView):
    template_name = 'login.html'
    form_class = Login
    redirect_authenticated_user = True


class ProfilePage(UpdateView):
    template_name = "profile.html"
    form_class = ProfileForm
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context

    def get_initial(self):
        user = self.request.user
        return {"bio": user.bio, "email": user.email, "profile_photo": user.profile_photo}

    def get_success_url(self):
        return f'/profile/{self.kwargs["pk"]}'









