from django.test import TestCase, Client
from django.urls import reverse, resolve
from apps.home.views import HomeView


class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_request_in_uls_home(self):
        request_url = reverse("home")
        self.assertEqual(request_url, "/")

    def test_home_view_called(self):
        response = self.client.get(reverse("home"))
        # Verifica se a view correta é chamada
        self.assertEqual(response.resolver_match.func.view_class, HomeView)

    def test_if_view_return_status_code_ok(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_usado(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home/home.html")
