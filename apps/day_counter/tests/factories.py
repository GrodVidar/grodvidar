import uuid

from factory import LazyAttribute, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from apps.users.models import User

from ..models import Counter

faker = Faker()


class UserFactory(DjangoModelFactory):
    username = LazyAttribute(lambda x: faker.word())

    class Meta:
        model = User


class CounterFactory(DjangoModelFactory):
    title = LazyAttribute(lambda x: faker.word())
    guid = LazyAttribute(lambda x: uuid.uuid4())
    create_date = faker.past_date()
    modify_date = faker.past_date()
    end_date = faker.future_date()
    user = SubFactory(UserFactory)

    class Meta:
        model = Counter
