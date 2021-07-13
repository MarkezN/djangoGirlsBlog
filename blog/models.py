from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):

	autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	naziv = models.CharField(max_length=200)
	tekst = models.TextField()
	datum_kreiranja = models.DateTimeField(default=timezone.now)
	datum_objave = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.datum_objave = timezone.now()
		self.save()


	def __str__(self):	
		return self.naziv



		
	# Create your models here.
