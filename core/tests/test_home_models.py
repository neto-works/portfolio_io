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
        # passamos 1 id eo restodas informações
        contato = Contato(1,self.data_mock)
        contato.save()

        quant_carc: bool = True if len(contato.nome) <= 65 else False # resultado_se_verdadeiro if condição else resultado_se_falso
        contato_exist_in_db: bool = True if (contato.nome != self.data_mock["nome"]) else False
        self.assertEquals(contato_exist_in_db,quant_carc)
