from django.shortcuts import render, HttpResponse,get_object_or_404
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    user = get_object_or_404(User, username='denis')
    return render(request, 'core/home.html',{'user':user})

def about(request):
    user=get_object_or_404(User, username='denis')
    return render(request, 'core/about.html', {'user':user})

def contacto(request):
    user = get_object_or_404(User, username='denis')
    return render(request, 'core/contact.html', {'user':user})