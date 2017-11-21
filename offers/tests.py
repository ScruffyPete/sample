from django.test import TestCase

from clients.models import Client
from offers.models import Offer


class OfferModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client.objects.create(name='Test client')
        cls.offer = Offer.objects.create(client=cls.client)

    def test_string_representation(self):
        self.assertEqual(str(self.offer), 'Oferta klienta {offer.client} dodana {offer.create_date}'.format(offer=self.offer))

    def test_verbose_name(self):
        self.assertEqual(str(Offer._meta.verbose_name), 'Oferta')

    def test_verbose_name_plural(self):
        self.assertEqual(str(Offer._meta.verbose_name_plural), 'Oferty')
