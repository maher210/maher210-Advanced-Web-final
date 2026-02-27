from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("student", "book", "rating")
    search_fields = ("student__username", "book__title")
    list_filter = ("rating",)
