from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from clients.models import Client, Adviser
from offers.models import Offer


class ClientModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client_obj = Client.objects.create(name='Test client_obj')

    def test_string_representation(self):
        self.assertEqual(str(self.client_obj), self.client_obj.name)

    def test_verbose_name(self):
        self.assertEqual(str(Client._meta.verbose_name), 'Klient')

    def test_verbose_name_plural(self):
        self.assertEqual(str(Client._meta.verbose_name_plural), 'Klienci')


class ClientViewSetTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        c1 = Client.objects.create(name='John Smith'),
        Client.objects.create(name='John Lennon'),
        Client.objects.create(name='Mark Brown'),

        for client in Client.objects.all():
            Offer.objects.create(client=client)
            client.advisers.add(Adviser.objects.create(name='Adviser for {}'.format(client)))
            client.advisers.add(Adviser.objects.create(name='Adviser for {}'.format(c1)))

    def test_list(self):
        response = self.client.get('/clients/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Client.objects.count())

    def test_list_filter_name(self):
        response = self.client.get('/clients/?name=john')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Client.objects.filter(name__icontains='john').count())

    def test_list_filter_offer(self):
        offer_id = Offer.objects.first().id
        response = self.client.get('/clients/?offer={}'.format(offer_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Client.objects.filter(offer=offer_id).count())

    def test_list_filter_adviser(self):
        adviser = Adviser.objects.first()
        response = self.client.get('/clients/?adviser={}'.format(adviser.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Client.objects.filter(pk__in=adviser.client_set.values('id')).count())

    def test_retrieve(self):
        client_id = Client.objects.first().id
        response = self.client.get('/clients/{}/'.format(client_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], client_id)

    def test_create(self):
        response = self.client.post('/clients/', {'name': 'Test Client'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_patch(self):
        client_id = Client.objects.first().id
        response = self.client.patch('/clients/{}/'.format(client_id), {'name': 'New Test Client'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        client_id = Client.objects.first().id
        response = self.client.delete('/clients/{}/'.format(client_id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

