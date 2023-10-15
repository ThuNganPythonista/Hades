import graphene
from graphene_django import DjangoObjectType
from src.public.apps.home.models import Categories, Items, Img


class ItemsType(DjangoObjectType):
    class Meta:
        model = Items
        field = ("color", "title", "price", "code", "discount", "description")

class Query(graphene.ObjectType):
    list_items=graphene.List(ItemsType)
    read_items = graphene.Field(ItemsType, id=graphene.Int()) # id=graphene.Int() gives id an integer datatype

    def resolve_list_items(root, info):
        return Items.objects.all()
    def resolve_read_items(root, info, id):
        return Items.objects.get(id=id)


schema = graphene.Schema(query=Query)
