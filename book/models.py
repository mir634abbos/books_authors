from django.db import models


class AuthorsModel(models.Model):
    tittle = models.CharField(max_length=200)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.tittle


class Book(models.Model):
    name = models.CharField(max_length=300)
    size = models.CharField(max_length=300)
    authors = models.ForeignKey(AuthorsModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=200)
    book = models.ManyToManyField(Book, related_name='Collections')

    def __str__(self):
        return self.name
