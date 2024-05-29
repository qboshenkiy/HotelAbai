from django.contrib import admin
from .models import Post, Card

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'image', 'created_at')  # Добавлено поле created_at

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'image', 'created_at')  # Добавлено поле created_at
