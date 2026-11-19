from rest_framework.test import APITestCase
from django.core.files.images import ImageFile

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
            title='Экскурсия',
            description_short='Коротко',
            description_long='Подробное описание',
        )
        self.entertainment = Entertainment.objects.create(
            title='Развлечение',
            description_short='Описание развлечения',
        )
        ExcursionPrice.objects.create(excursion=self.excursion, header='Взрослый', price=25)

    def test_list_contains_only_excursions(self):
        response = self.client.get('/api/excursions/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual([item['id'] for item in response.data], [self.excursion.id])
        self.assertEqual(response.data[0]['title'], 'Экскурсия')
        self.assertEqual(str(response.data[0]['prices'][0]['Взрослый']), '25.00')

    def test_retrieve_excursion(self):
        response = self.client.get(f'/api/excursions/{self.excursion.id}/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.excursion.id)
        self.assertEqual(response.data['description_long'], 'Подробное описание')
