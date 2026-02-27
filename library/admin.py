from django.contrib import admin
from .models import Book, Author, Category
from reviews.models import Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    readonly_fields = ("student", "rating", "comment")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "available_copies",
        "total_copies",
    )

    search_fields = ("title", "author__name")
    list_filter = ("category", "author")
    inlines = [ReviewInline]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)