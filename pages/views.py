from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from library.models import Book, Author, Category
from django.db.models import Avg
from django.contrib.auth.models import User
from .forms import ContactForm
from django.db.models import Count

@login_required
def home(request):
    latest_books = Book.objects.order_by('-id')[:6]

    top_books = (
        Book.objects
        .annotate(avg_rating=Avg('review__rating'))
        .order_by('-avg_rating')[:3]
    )

    stats = {
        "books": Book.objects.count(),
        "authors": Author.objects.count(),
        "categories": Category.objects.count(),
        "students": User.objects.filter(is_staff=False).count(),
    }

    context = {
        "latest_books": latest_books,
        "top_books": top_books,
        "stats": stats,
    }

    return render(request, "pages/home.html", context)

def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
           
            return render(request, "pages/contact_success.html")

    return render(request, "pages/contact.html", {"form": form})

def authors(request):
    authors = Author.objects.annotate(
        books_count=Count("book")
    )

    return render(request, "pages/authors.html", {
        "authors": authors
    })