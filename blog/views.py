from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime

# Create your views here.

def home(request):
	text = """<h1>Bienvenue sur mon blog!</h1>"""
	return HttpResponse(text)


def view_article(request, id_article):
	if int(id_article) > 100:
		raise Http404

	elif int(id_article) == 42:
		return redirect(view_redirection)

	return HttpResponse(
		"Voici l'article {0}".format(id_article))



def list_articles(request, month, year):
	return HttpResponse(
		"Les articles de {0} {1}".format(month, year))



def view_redirection(request):
	return HttpResponse(
		"Vous avez été redirigé")

def date_actuelle(request):
	return render(request, 'blog/date.html', {'date' :  datetime.now()})