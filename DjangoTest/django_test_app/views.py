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


def home(request):
    a = Post.objects.all()
    return render(request, 'home.html', {'posts': a, 'title': 'Home', 'user': request.user})


class HomePage(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'post'


class Js(TemplateView):
    template_name = "js.html"



def form_page(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=name, email=email, password=password)
            user.save()
            return redirect('/')
    else:
        return render(request, 'registration.html', {'form': Registration()})


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


class CreateComment(TemplateView):
    template_name = "post.html"

    def post(self, request, **kwargs):
        data = request.POST
        if data.get['post']:
            pass
        elif data['post']:
            #update_post
            pass
        return redirect()

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs["id"])
        return super().form_valid(form)

    def get_success_url(self):
        return f'/post/{self.kwargs["id"]}'


class PostCreate(CreateView):
    form_class = PostForm
    template_name = 'postcreate.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowPost(TemplateView):
    template_name = "post.html"
    # model = Post
    # form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(id=self.kwargs["id"])
        context['post'] = post
        context['comment'] = Comment.objects.filter(post=post)
        return context


def post_page(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            post = Post(text=text, user=request.user)
            post.save()
            return redirect("home")
            print(text)
    else:
        return render(request, "post.html", {"form": PostForm()})


def user_page(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            age = form.cleaned_data['age']
            print(name, surname, age)
    else:
        return render(request, 'form.html', {'form': UserForm()})


@login_required
def logout_view(request):
    logout(request)
    return redirect('/login')


class LoginPage(LoginView):
    template_name = 'login.html'
    form_class = Login
    redirect_authenticated_user = True


@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user, 'profile': Profile.objects.get(user=request.user)})


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


class ajaxpage(TemplateView):
    template_name = 'page.html'

    def post(self, request):
        print(request.POST)
        return JsonResponse({'status': 'OK'})






