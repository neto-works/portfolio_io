from django.test import TestCase
from model_mommy import mommy
from apps.home.models import Contato

class HomeModelTest(TestCase):
    def setUp(self):
        self.contato = mommy.make(Contato)
        
    def test_testing_whether_the_models_str_is_returned_correctly(self):
        self.assertEquals(self.contato.email, self.contato.__str__())