from django.shortcuts import render, redirect
from .models import MiniUrl

# Create your views here.


def home(request):
	urls = MiniUrl.objects.all()
	return render(request, 'home.html', {'urls':urls})


def redirection(request, code):
	return redirect('https://openclassrooms.com/courses')