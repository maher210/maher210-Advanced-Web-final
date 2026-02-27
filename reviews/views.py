from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from library.models import Book
from .models import Review


@login_required(login_url="/")
def add_review(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        Review.objects.create(
            student=request.user,
            book=book,
            rating=request.POST['rating'],
            comment=request.POST['comment']
        )
        return redirect('book_detail', id)
    return render(request, 'reviews/add_review.html', {'book': book})


