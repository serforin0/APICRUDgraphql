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


#************************ Student - mutations *************#


class CreateStudent(graphene.Mutation):

  
  class Arguments:
    name = graphene.String()
    age = graphene.Int()
    degree = graphene.List(graphene.ID) 
    date_created = graphene.types.datetime.DateTime()

  # What it returns
  student = graphene.Field(StudentType)

  
  def mutate(self, info, name, age=None, degree=None, date_created=None):
    student = Student.objects.create(
      name = name,
      age = age,
      date_created = date_created
    )

    
    if degree is not None:
      degree_set = []
      for degree_id in degree:
        degree_object = Degree.objects.get(pk=degree_id)
        degree_set.append(degree_object)
      student.degree.set(degree_set)

    student.save()
   
    return CreateStudent(
      degree=degree
    )

class UpdateStudent(graphene.Mutation):
  
  class Arguments:
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()
    degree = graphene.List(graphene.ID)
    date_created = graphene.types.datetime.DateTime()

  
  student = graphene.Field(StudentType)



  def mutate(self, info, id, name=None, age=None, degree=None, date_created=None):
    student = Product.objects.get(pk=id)
    student.name = name if name is not None else student.name
    student.age = age if age is not None else student.age
    student.date_created = date_created if date_created is not None else student.date_created

    
    if degree is not None:
      degree_set = []
      for degree_id in degree:
        degree_object = degree.objects.get(pk=degree_id)
        degree_set.append(degree_object)
      student.degree.set(degree_set)

    student.save()
    
    return UpdateStudent(student=student)


class DeleteStudent(graphene.Mutation):
  class Arguments:
    
    id = graphene.ID()

  
  student = graphene.Field(StudentType)

  def mutate(self, info, id):
    student = Student.objects.get(pk=id)
    if student is not None:
      student.delete()
    return DeleteStudent(student=student)


class Mutation(graphene.ObjectType):
  create_student = CreateStudent.Field()
  update_student = UpdateStudent.Field()
  delete_student = DeleteStudent.Field()




# class Query(graphene.ObjectType):
# 	students = graphene.List(StudentType)
	
# 	def resolve_students(self, info, **kwargs):
# 		return Student.objects.all()
