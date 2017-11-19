from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from model_mommy import mommy

from beers.models import Company


# class CompanyListViewTest(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         Company.objects.create(name="comp1", tax_number=1)
#         Company.objects.create(name="comp2", tax_number=2)
#         Company.objects.create(name="comp3", tax_number=3)
#         User.objects.get_or_create(username="pepe")
#
#     def test_view_url_not_accessible(self):
#         url = '/company/list/'
#         resp = self.client.get(url)
#         self.assertEqual(resp.status_code, 302)
#
#     def test_view_url_exists_at_desired_location(self):
#         url = '/company/list/'
#         self.client.force_login(User.objects.first())
#         resp = self.client.get(url)
#         self.assertEqual(resp.status_code, 200)
#
#     def test_view_returns_all_entries(self):
#         url = '/company/list/'
#         self.client.force_login(User.objects.first())
#         resp = self.client.get(url)
#         self.assertEqual(resp.context['object_list'].count(), Company.objects.all().count())
#
#     def test_redirect_if_not_logged_in(self):
#         resp = self.client.get(reverse('company-list-view'))
#         self.assertRedirects(resp, '/accounts/login/?next=/company/list/')
#
#     def test_logged_in_uses_correct_template(self):
#         self.client.force_login(User.objects.first())
#         resp = self.client.get(reverse('company-list-view'))
#         self.assertTemplateUsed(resp, 'beer/company_list.html')


class CompanyListViewMommyApproach(TestCase):

    def setUp(self):
        self.user = mommy.make(User)
        self.attachments = mommy.make(Company,_quantity=5)

    def test_view_url_not_accessible(self):
        url = '/company/list/'
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)

    def test_view_url_exists_at_desired_location(self):
        url = '/company/list/'
        self.client.force_login(User.objects.first())
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_view_returns_all_entries(self):
        url = '/company/list/'
        self.client.force_login(User.objects.first())
        resp = self.client.get(url)
        self.assertEqual(resp.context['object_list'].count(), Company.objects.all().count())

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('company-list-view'))
        self.assertRedirects(resp, '/accounts/login/?next=/company/list/')

    def test_logged_in_uses_correct_template(self):
        self.client.force_login(User.objects.first())
        resp = self.client.get(reverse('company-list-view'))
        self.assertTemplateUsed(resp, 'beer/company_list.html')
