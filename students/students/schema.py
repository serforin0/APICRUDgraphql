import graphene

from students.apps.usuarios import schema


class Query(schema.Query, graphene.ObjectType):
	pass

class Mutation(schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)