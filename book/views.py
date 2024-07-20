from django.shortcuts import render
from .models import Collection, Book, AuthorsModel


def collection(request):
    collects = Collection.objects.all()
    return render(request, 'collection.html', {'collections': collects})
