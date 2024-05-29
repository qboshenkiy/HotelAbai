from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('send-feedback/', views.send_feedback_email, name='send_feedback_email')
]