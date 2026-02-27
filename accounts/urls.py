from django.urls import path
from . import views
from .views import profile_view

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
    path("edit/", views.edit_profile, name="edit_profile"),

]