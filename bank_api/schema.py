import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from banks.models import Branch, Bank
import django_filters

# Step 1: Define your Relay-compatible GraphQL types
class BankType(DjangoObjectType):
    class Meta:
        model = Bank
        interfaces = (relay.Node,)
        fields = "__all__"

class BranchType(DjangoObjectType):
    class Meta:
        model = Branch
        interfaces = (relay.Node,)
        fields = "__all__"

# Step 2: Create a FilterSet with allowed filter fields
class BranchFilterSet(django_filters.FilterSet):
    class Meta:
        model = Branch
        fields = ['bank__name', 'ifsc', 'branch', 'city', 'state']

# Step 3: Define your GraphQL query class
class Query(graphene.ObjectType):
    branches = DjangoFilterConnectionField(BranchType, filterset_class=BranchFilterSet)

# Step 4: Create the schema
schema = graphene.Schema(query=Query)
