from django.db import models

# Create your models here.
class Producto(models.Model):
	title = models.CharField(max_length=50)
	supplier = models.CharField(max_length=50)
	description = models.TextField(max_length=50)
	price = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title