from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import datetime
from blog.models import Article

# Create your views here.

def home(request):
	articles = Article.objects.all()
	return render(request, 'blog/accueil.html', {'derniers_articles': articles})



def lire(request, id, slug):
	article = get_object_or_404(Article, id = id, slug = slug)
	return render(request, 'blog/lire.html', {'article' : article})
