import factory
from grants.models.grant_type import GrantType


class GrantTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GrantType
