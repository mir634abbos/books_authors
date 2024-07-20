from django.urls import path
from book.views import collection
urlpatterns = [
    path('', collection, name='collection')
]
