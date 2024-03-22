from django.test import TestCase
from model_mommy import mommy
from apps.home.models import Contato


class HomeModelTest(TestCase):
    def setUp(self):
        self.data_mock = {
            "nome": "marcos dantas",
            "cidade": "Caicó",
            "email": "marcos_dantas@gmail.com",
            "telefone": "8491958487",
            "descricao": "Um textão",
        }
        self.contato = mommy.make(Contato)

    def test_whether_the_models_str_is_returned_correctly(self):
        self.assertEquals(self.contato.nome, self.contato.__str__())

    def test_contato_title_raises_error_if_title_has_more_than_65_chars(self):
        contato = Contato(1, self.data_mock)
        contato.save()

        quant_carc: bool = (True if len(contato.nome) <= 65 else False)
        contato_exist_in_db: bool = (True if (contato.nome != self.data_mock["nome"]) else False)
        self.assertEquals(contato_exist_in_db, quant_carc)

    def test_model_contain_field(self):
        self.assertTrue(hasattr(self.contato, 'nome'))
        self.assertTrue(hasattr(self.contato, 'cidade'))
        self.assertTrue(hasattr(self.contato, 'email'))
        self.assertTrue(hasattr(self.contato, 'cidade'))
        self.assertTrue(hasattr(self.contato, 'telefone'))
        self.assertTrue(hasattr(self.contato, 'descricao'))

    def test_model_contain_6_field(self):
        todos_fields = [fields.name for fields in self.contato._meta.get_fields()]
        self.assertEqual(len(todos_fields), 6)
