from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from library.models import Book
from .models import Borrow
from datetime import date
from django.utils import timezone
import datetime




@login_required(login_url="/")
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)


    if book.available_copies == 0:
        messages.error(request, 'الكتاب غير متوفر')
        return redirect('book_detail', book_id)


    Borrow.objects.create(
        student=request.user,
        book=book,
       expected_return_date = timezone.now().date() + datetime.timedelta(days=14)
        )
    book.available_copies -= 1
    book.save()

    messages.success(request, 'تمت الاستعارة بنجاح')
    return redirect('my_books')

@login_required(login_url="/")
def return_book(request, borrow_id):
    borrow = get_object_or_404(
        Borrow,
        id=borrow_id,
        student=request.user,
        return_date__isnull=True
    )

    borrow.return_date = timezone.now()
    borrow.save()

    book = borrow.book
    book.available_copies += 1
    book.save()

    return redirect('my_books')

@login_required(login_url="/")
def my_books(request):
    borrows = Borrow.objects.filter(
        student=request.user,
        return_date__isnull=True
    )

    for b in borrows:
        b.remaining_days = (b.expected_return_date - date.today()).days
        b.is_late = b.remaining_days < 0

    return render(request, "borrowing/my_books.html", {
        "borrows": borrows
    })



