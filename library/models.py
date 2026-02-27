from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField()
    photo = models.ImageField(upload_to='authors/', null=True, blank=True)


    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    publication_year = models.IntegerField()
    pages = models.IntegerField()
    language = models.CharField(max_length=50)
    total_copies = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField()
    cover = models.ImageField(upload_to='books/')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title