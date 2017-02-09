from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.home, name= 'home'),
	url(r'^redirect/(?P<code>.+)$', views.redirection, name= 'redirection'),
	
]