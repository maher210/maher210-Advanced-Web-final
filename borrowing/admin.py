from django.contrib import admin
from .models import Borrow

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "book",
        "borrow_date",
        "return_date",
    )

    search_fields = ("student__username", "book__title")
    list_filter = ("borrow_date", "return_date")
