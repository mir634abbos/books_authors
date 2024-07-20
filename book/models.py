from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=300)
    size = models.CharField(max_length=300)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=200)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
