from django.shortcuts import render,get_object_or_404
from .models import Book, Category
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Avg
from borrowing.models import Borrow
from reviews.models import Review


@login_required(login_url="/")
def books(request):
    books_qs = Book.objects.select_related("author", "category").all()
    categories = Category.objects.all()

    
    search = request.GET.get("search")
    if search:
        books_qs = books_qs.filter(title__icontains=search)

    category_id = request.GET.get("category")
    if category_id and category_id.isdigit():
        books_qs = books_qs.filter(category_id=int(category_id))

   
    paginator = Paginator(books_qs, 6)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "categories": categories,
        "search": search,
        "category_id": category_id,
    }

    return render(request, "library/books.html", context)



@login_required(login_url="/")
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)


    reviews = Review.objects.filter(book=book).select_related("student")
   
    avg_rating = reviews.aggregate(avg=Avg("rating"))["avg"]
    
    user_borrow = Borrow.objects.filter(
    student=request.user,
    book=book,
    return_date__isnull=True
    ).first()

    context = {
        "book": book,
        "reviews": reviews,
        "avg_rating": avg_rating,
        "user_borrow": user_borrow,
    }

    return render(request, "library/book_detail.html", context)

@login_required(login_url="/")
def home(request):
    books = Book.objects.all()[:6]  
    return render(request, "library/home.html", {"books": books})