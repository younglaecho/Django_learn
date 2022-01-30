from django.contrib import admin
from books.models import Book, Author, Publisher
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
  fields = ['name', 'salutation', 'email']
admin.site.register(Book)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher)

