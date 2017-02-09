from django.db import models

# Create your models here.

class MiniUrl(models.Model):
	url= models.URLField(max_length= 100)
	code= models.CharField(max_length= 10, unique= True)
	date= models.DateTimeField(auto_now_add= True, auto_now= False)
	pseudo= models.CharField(max_length= 40, blank= True)
	nb_acces= models.IntegerField(default= 0)
