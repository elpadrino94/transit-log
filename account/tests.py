from django.test import TestCase
from django.urls import reverse


class RegisterViewTests(TestCase):
    def test_register_page_contains_full_name_field(self):
        response = self.client.get(reverse('register'))

        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertContains(response, 'name="full_name"')
        self.assertContains(response, 'Nom complet')
