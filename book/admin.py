from django.contrib import admin

from .models import AuthorsModel, Book, Collection


admin.site.register(AuthorsModel)
admin.site.register(Book)
admin.site.register(Collection)
