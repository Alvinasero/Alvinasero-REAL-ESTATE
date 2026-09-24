from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class PropertyPermissionTests(TestCase):
    def test_public_property_pages_are_available(self):
        response = self.client.get(reverse('property_list'))

        self.assertEqual(response.status_code, 200)

    def test_anonymous_users_are_redirected_from_property_management(self):
        response = self.client.get(reverse('manage_properties'))

        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response['Location'])

    def test_customer_users_cannot_manage_properties(self):
        user = get_user_model().objects.create_user(
            username='customer',
            password='pass12345',
            role='customer',
        )
        self.client.force_login(user)

        response = self.client.get(reverse('manage_properties'))

        self.assertEqual(response.status_code, 403)

    def test_admin_role_users_can_manage_properties(self):
        user = get_user_model().objects.create_user(
            username='adminuser',
            password='pass12345',
            role='admin',
        )
        self.client.force_login(user)

        response = self.client.get(reverse('manage_properties'))

        self.assertEqual(response.status_code, 200)
