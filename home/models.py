from django.db import models

class BusSystem(models.Model):
	bus = models.CharField(max_length=40)
	diesel = models.DecimalField(max_digits=10, decimal_places=3)
	qty = models.FloatField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	date = models.DateField(auto_now=False, auto_now_add=False)