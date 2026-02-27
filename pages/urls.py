from django.urls import path
from .views import contact
from .views import authors

urlpatterns = [
    path("contact/", contact, name="contact"),
    path("authors/", authors, name="authors"),
]