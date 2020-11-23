import graphene
from graphene import Argument
from graphene_django import DjangoObjectType
from .models import *



class StudentType(DjangoObjectType):
	class Meta:
		model = Student

class DegreeType(DjangoObjectType):
	class Meta:
		model =  Degree


class Query(graphene.ObjectType):
	all_student = graphene.List(StudentType)
	student = graphene.Field(StudentType, id=graphene.ID())

	all_degree =  graphene.List(DegreeType)
	degree = graphene.Field(DegreeType, id=graphene.ID())

	def resolve_all_student(self, info, **kwargs):
		# Querying a list of students
		return Student.objects.all()

	def resolve_student(self, info, id):
		#Querying a single student
		return Student.objects.get(pk=id)

	def resolve_all_degree(self, info, **kwargs):
		#Querying a list of degree
		return Degree.objects.all()




# class Query(graphene.ObjectType):
# 	students = graphene.List(StudentType)
	
# 	def resolve_students(self, info, **kwargs):
# 		return Student.objects.all()
