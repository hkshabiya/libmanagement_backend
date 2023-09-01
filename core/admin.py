from django.contrib import admin
from .models import Category
from .models import Book
from .models import AssignedBook

# Register your models here.
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(AssignedBook)
