from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from accounts import views as account_views
from library.views import books, book_detail
from borrowing.views import borrow_book, my_books,return_book
from reviews.views import add_review
from pages.views import home



urlpatterns = [
    path('admin/', admin.site.urls),   
    path("", account_views.login_view, name="login"),
    path("home/", home, name="home"),  # الصفحة الرئيسية بعد تسجيل الدخول
    path('books/', books, name='books'),
    path('book/<int:id>/', book_detail, name='book_detail'),
    path('borrow/<int:book_id>/', borrow_book, name='borrow_book'),
    path('my-books/', my_books, name='my_books'),
    path('book/<int:id>/review/', add_review, name='add_review'),
    path("return/<int:borrow_id>/", return_book, name="return_book"),
    path("", include("accounts.urls")),
    path("pages/", include("pages.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)