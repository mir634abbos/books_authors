from django.shortcuts import render
from .models import Collection


def collection(request):
    collects = Collection.objects.prefetch_related('book__authors').all()
    return render(request, 'collection.html', {'collections': collects})
