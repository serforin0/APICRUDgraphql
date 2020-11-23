from django.db import models
from django.utils.translation import gettext as _


class Student(models.Model):
	name = models.CharField(max_length=50, unique=True)
	age = models.IntegerField()
	degree = models.ManyToManyField("degree", blank=True)
	date_created = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)

	def __str__(self):
		return self.name

class Degree(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name
