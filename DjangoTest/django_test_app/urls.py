from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("fourth/", views.form_page, name='fourth'),
    path("user/", views.user_page, name="user"),
    path('home/', views.HomePage.as_view(), name='home'),
    path("showpost/<int:id>/", views.ShowPost.as_view(), name="getpost"),
    path("post/<int:pk>/", views.PostPage.as_view(), name="post"),
    path("postpage/", views.post_page, name="postpage"),
    path("registration/", views.RegistrationPage.as_view(), name="registration"),
    path("logout/", views.logout_view, name="logout"),
    path("login/", views.LoginPage.as_view(), name="login"),
    path("postcreate/", views.PostCreate.as_view(), name="createpost"),
    path("create_comment<int:id>/", views.CreateComment.as_view(), name="createcomment"),
    path("profile/<int:pk>/", views.ProfilePage.as_view()),
    path("js/", views.Js.as_view(), name="js"),
    path("ajax/", views.ajaxpage.as_view())]
