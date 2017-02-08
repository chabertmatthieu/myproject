from django.contrib import admin
from django.utils.text import Truncator
from .models import Article, Categorie





class ArticleAdmin(admin.ModelAdmin):
	list_display = ('titre', 'auteur', 'date', 'apercu_contenu')
	list_filter = ('auteur', 'categorie',)
	ordering = ('date',)
	search_fields = ('titre', 'contenu')
	date_hierarchy = 'date'
	prepopulated_fields = {'slug': ('titre',),}

	fieldsets = (
		('Général', {
			'fields' : ('titre', 'slug', 'auteur', 'categorie')
		}),
		('Contenu de l\'article', {
			'description' : ('Le formulaire accepte les balises HTML.'),
			'fields' : ('contenu',)

			}),
		)

	def apercu_contenu(self, article):
		return Truncator(article.contenu).chars(40, truncate= '...')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie)
