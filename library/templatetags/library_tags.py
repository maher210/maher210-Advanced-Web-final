from django import template
register = template.Library()


@register.filter
def book_status(book):
    return 'Available' if book.available_copies > 0 else 'Borrowed'