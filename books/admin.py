from django.contrib import admin
from .models import Category, Book, Author, Favorite

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Favorite)
