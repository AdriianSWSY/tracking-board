import factory
from factory import Faker, SubFactory

from apps.users.tests.factories import UserFactory


class BoardFactory(factory.django.DjangoModelFactory):
    name = Faker("name")
    creator = SubFactory(UserFactory)

    class Meta:
        model = "board.Board"
