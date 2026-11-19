from rest_framework.test import APITestCase
from django.core.files.images import ImageFile
from django.urls import reverse

from entertainments.serializers import *
from entertainments.models import *


class NearestAPITestCase(APITestCase):

    def setUp(self):
        self.nearest_1 = NearestPlace.objects.create(
            title='test nearest 1',
            description='test description',
            location='test location'
        )
        self.nearest_2 = NearestPlace.objects.create(
            title='test nearest 2',
            description='test description',
            location='test location'
        )
        self.photo_1 = PhotoNearestPlace.objects.create(
            file=ImageFile(open("tests_media/mesye.png", "rb")),
            places=self.nearest_1
        )

    def test_get(self):
        url = 'http://127.0.0.1:8000/api/nearests/'
        response = self.client.get(url)
        phoros_list = response.data[0]['photos']
        self.assertEqual(response.status_code, 200)
        self.assertTrue(phoros_list[0])


class ExcursionAPITestCase(APITestCase):

    def setUp(self):
        self.excursion = Excursion.objects.create(
            title='Тестовая экскурсия',
            description_short='Короткое описание',
            description_long='Полное описание',
        )
        self.entertainment = Entertainment.objects.create(
            title='Тестовое развлечение',
            description_short='Описание развлечения',
        )
        ExcursionPrice.objects.create(
            excursion=self.excursion,
            header='Взрослый билет',
            price=35,
        )

    def test_list_returns_only_excursions_and_related_prices(self):
        response = self.client.get(reverse('excursion-list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual([item['id'] for item in response.data], [self.excursion.id])
        self.assertEqual(response.data[0]['title'], 'Тестовая экскурсия')
        self.assertEqual(response.data[0]['photos'], [])
        self.assertEqual(
            str(response.data[0]['prices'][0]['Взрослый билет']),
            '35.00',
        )
        self.assertEqual(Entertainment.objects.count(), 1)
        self.assertEqual(Excursion.objects.count(), 1)

    def test_retrieve_returns_excursion_details(self):
        response = self.client.get(
            reverse('excursion-detail', kwargs={'pk': self.excursion.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.excursion.id)
        self.assertEqual(response.data['description_long'], 'Полное описание')
