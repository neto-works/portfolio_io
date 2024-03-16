from django.test import TestCase
from apps.home.forms import ContatoForm


class ContatoFormTest(TestCase):
    def setUp(self):
        self.data_certa = {
            "nome": "Jonas Cabrini",
            "cidade": "São João do sabugi",
            "email": "Jonas.brtp@gmail.com",
            "telefone": "81218541",
            "descricao": "Um textão",
        }
        self.data_errada = {
            "cidade": "São João do sabugi",
            "email": "Jonas.brtp",
            "telefone": "81218541",
            "descricao": "Um textão",
        }
        self.data_faltante = {
            "cidade": "São João do sabugi",
            "telefone": "81218541",
            "descricao": "Um textão",
        }

    def test_fields_exists(self):
        self.form = ContatoForm(self.data_certa)
        self.assertEquals(len(self.form.fields), 5)

    def test_if_the_form_is_filled_out_correctly_if_it_is_valid(self):
        self.form = ContatoForm(self.data_certa)
        self.assertTrue(self.form.is_valid)
