from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from application import models


class ItemType(DjangoObjectType):
    class Meta:
        model = models.Item


class Query(graphene.ObjectType):
    items = graphene.List(ItemType)

    def resolve_items(root, info):
        return (
            models.Item.objects.all()
        )


schema = graphene.Schema(query=Query)