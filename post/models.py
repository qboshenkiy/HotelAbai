from django.db import models
from django.utils import timezone

class Post(models.Model):
    category = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/image/")
    created_at = models.DateTimeField(default=timezone.now)  # Задайте значение по умолчанию

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']  # Сортировка по возрастанию даты добавления

class Card(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField(max_length=255)
    image = models.ImageField(upload_to="media/image/")
    created_at = models.DateTimeField(default=timezone.now)  # Задайте значение по умолчанию

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # Сортировка по возрастанию даты добавления
