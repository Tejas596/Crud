from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'author')
