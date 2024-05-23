from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomePage.as_view(), name='home'),
    path("post/<int:pk>/", views.PostPage.as_view(), name="post"),
    path('post/<int:pk/comment_create/', views.CommentCreate.as_view()),
    path('post/<int:pk>/update_post', views.PostUpdate.as_view()),
    path("registration/", views.RegistrationPage.as_view(), name="registration"),
    path("logout/", views.logout_view, name="logout"),
    path("login/", views.LoginPage.as_view(), name="login"),
    path("postcreate/", views.PostCreate.as_view(), name="createpost"),
    path("profile/<int:pk>/", views.ProfilePage.as_view())
]
