from django.test import TestCase
from .factories import CounterFactory, UserFactory
from datetime import date, time
from django.db import IntegrityError


def test_delete():
    counter = CounterFactory.build(id=1)
    counter.delete()


class ModelsTestCase(TestCase):
    def test_string_representation(self):
        counter = CounterFactory.build(title='My Test Counter', id=1)
        self.assertEqual(str(counter), '1: My Test Counter')

    def test_save(self):
        counter = CounterFactory(end_date=date.today())
        self.assertTrue(counter.is_date_only)
        self.assertEqual(counter.end_time, time(0, 0))

    def test_uniqueness(self):
        user = UserFactory()
        CounterFactory(title='My unique title', user=user, is_guest=False)
        with self.assertRaises(IntegrityError):
            CounterFactory(title='My unique title', user=user, is_guest=False)

