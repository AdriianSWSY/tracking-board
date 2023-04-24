import factory
from factory import Faker, SubFactory

from apps.board.tests.factories import BoardFactory
from apps.users.tests.factories import UserFactory


class ColumnFactory(factory.django.DjangoModelFactory):
    name = Faker("name")
    board = SubFactory(BoardFactory)
    creator = SubFactory(UserFactory)

    class Meta:
        model = "columns.Column"
