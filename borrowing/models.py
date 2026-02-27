from django.db import models
from django.contrib.auth.models import User
from library.models import Book


class Borrow(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    expected_return_date = models.DateField()

    def __str__(self):
     return f"{self.student} - {self.book}"
