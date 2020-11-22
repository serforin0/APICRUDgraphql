import graphene
from graphene_django import DjangoObjectType
from .models import *


class StudentType(DjangoObjectType):
	class Meta:
		model = Student


class Query(graphene.ObjectType):
	students = graphene.List(StudentType)
	
	def resolve_students(self, info, **kwargs):
		return Student.objects.all()
