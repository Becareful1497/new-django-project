from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'price', 'created_at')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('genre', 'language', 'published_date')
