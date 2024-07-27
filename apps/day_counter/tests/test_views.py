from django.test import TestCase
from django.urls import reverse

from .factories import CounterFactory, UserFactory


class CounterViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.user = UserFactory()
        cls.counter_with_user = CounterFactory(user=cls.user)
        cls.counter_without_user = CounterFactory()

    def test_counter_detail(self):
        url = reverse('counters:counter_view', kwargs={'guid': self.counter_without_user.guid})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_counter_list(self):
        url = reverse('counters:counters_view')
        self.client.force_login(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
