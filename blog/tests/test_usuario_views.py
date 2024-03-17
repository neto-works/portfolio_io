from django.test import TestCase, Client
from django.urls import reverse, resolve
from apps.usuario import views


class TestUsuarioView(TestCase):
    def setUp(self):
        self.cliente = Client()
        self.url_test = "/register/"

    def test_url_create_usuario_is_correct(self):
        create_url = reverse("registre_se")
        self.assertEqual(create_url, "/register/")

    def test_if_view_return_status_code_ok(self):
        response = self.cliente.get(reverse("registre_se"))
        self.assertEqual(response.status_code, 200)

    def test_function_reateuser_view_is_the_function_that_responds_when_url_registre_se_is_called(
        self,
    ):
        oneview = resolve("/register/")
        self.assertIs(oneview.func, views.createuser_view)

    def test_templates_used(self):
        with self.assertTemplateUsed("index.html"):
            response = self.cliente.get(self.url_test)
        with self.assertTemplateUsed("partials/head.html"):
            response = self.cliente.get(self.url_test)
        with self.assertTemplateUsed("partials/footer.html"):
            response = self.cliente.get(self.url_test)
        with self.assertTemplateUsed("usuarios/register.html"):
            response = self.cliente.get(self.url_test)
