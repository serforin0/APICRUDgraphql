import graphene

from students.apps.usuarios import schema


class Query(schema.Query, graphene.ObjectType):
	pass


schema = graphene.Schema(query=Query)