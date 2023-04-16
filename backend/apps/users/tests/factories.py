import factory


class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker("first_name")
    email = factory.Faker("email")

    class Meta:
        model = "users.User"
