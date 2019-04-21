from django.test import TestCase
from rest_framework import status
from rest_framework.test import APISimpleTestCase


class ExchangeRateTests(APISimpleTestCase):
    fixtures = ['currencies.json']

    def test_available_conversions(self):
        """
        Tests whether API returns a list of available conversions
        """
        response = self.client.get('/v1/conversions')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [
            {'target': 'CAD', 'base': 'EUR'},
            {'target': 'GBP', 'base': 'EUR'},
            {'target': 'USD', 'base': 'EUR'}])

    def test_rate_history(self):
        """
        Tests history of a given exchange rate
        """
        response = self.client.get('/v1/history/EUR/GBP')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [
            {
                "rate": 0.8647,
                "at": "2019-04-21T19:49:35Z"
            },
            {
                "rate": 0.8539,
                "at": "2019-04-20T19:53:18Z"
            }
        ])

    def test_rate_history_chronolic(self):
        """
        Tests history of a given exchange rate
        """
        response = self.client.get('/v1/history/EUR/CAD')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [
            {
                "rate": 1.1599,
                "at": "2019-04-21T18:36:45Z"
            },
            {
                "rate": 1.1508,
                "at": "2019-04-21T19:36:29Z"
            },
        ])

    def test_no_history(self):
        """
        When there is no history API should return 404
        """
        response = self.client.get('/v1/history/EUR/WTF')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
