from django.db import models

# Create your models here.


class Article(models.Model):
	titre = models.CharField(max_length = 100)
	slug = models.CharField(max_length = 100)
	auteur = models.CharField(max_length = 42)
	contenu = models.TextField(null = True)
	date = models.DateTimeField(auto_now_add = True, auto_now = False, verbose_name = "Date de parution")

	categorie = models.ForeignKey('Categorie')

	def __str__(self):
		return self.titre


class Categorie(models.Model):
	nom = models.CharField(max_length = 40)

	def __str__(self):
		return self.nom


class Contact(models.Model):
	nom = models.CharField(max_length= 225)
	adresse = models.TextField()
	photo = models.ImageField(upload_to= 'photos/')

	def __str__(self):
		return self.nom
