from django.test import TestCase

from beers.models import Beer, Company


class BeerTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        company = Company.objects.create(name="comp", tax_number=1)
        Beer.objects.create(name="AlcBeer", abv = 4, company=company)
        Beer.objects.create(name="NonAlcBeer", abv = 0, company=company)

    def test_is_alcoholic(self):
        alcoholic_beer = Beer.objects.get(pk=1)
        self.assertEqual(alcoholic_beer.is_alcoholic, True)

    def test_is_non_alcoholic(self):
        non_alcoholic_beer = Beer.objects.get(pk=2)
        self.assertEqual(non_alcoholic_beer.is_alcoholic, False)

    def test_has_more_alcohol_than(self):
        alcoholic_beer = Beer.objects.get(pk=1)
        self.assertTrue(alcoholic_beer.has_more_alcohol_than(1))