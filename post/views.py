from django.shortcuts import render, redirect
from .models import Card, Post
from django.views.decorators.http import require_POST
from django.core.mail import send_mail

def index(request):
    posts = Post.objects.all()
    cards = Card.objects.all()
    context = {
        'posts': posts,
        'cards': cards
    }
    return render(request, 'main/index.html', context)

@require_POST
def send_feedback_email(request):
    phone = request.POST.get('phone', '')
    email = request.POST.get('email', '')
    name = request.POST.get('name', '')

    subject = 'Feedback from website'
    from_email = 'fittsqboshenkiy@gmail.com'
    to_email = 'fittsqboshenkiy@gmail.com'
    body = f'Phone: {phone}\nEmail: {email}\nName: {name}'

    send_mail(subject, body, from_email, [to_email])

    return redirect('index')
