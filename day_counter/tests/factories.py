from random import randint
import uuid

from django.db.models import BigIntegerField
from factory.django import DjangoModelFactory
from factory import LazyAttribute, SubFactory
from faker import Faker
from ..models import Counter
from users.models import User


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

