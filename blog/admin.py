from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)  # use of decorator

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']