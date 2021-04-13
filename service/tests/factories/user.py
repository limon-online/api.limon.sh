import factory

from apps.user import models as user_models


class UserFactory(factory.django.DjangoModelFactory):
    uuid = factory.Faker('uuid4')
    first_name = factory.Faker('word')
    last_name = factory.Faker('word')
    email = factory.Faker('email')
    password = factory.Faker('sentence')
    is_active = True
    is_superuser = False

    class Meta:
        model = user_models.User
