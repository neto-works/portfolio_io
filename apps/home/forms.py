from django import forms


class ContatoForm(forms.Form):
    cidade = forms.CharField(label="Cidade", max_length=254)
    email = forms.EmailField(label="E-mail", max_length=254)
    telefone = forms.CharField(label="Telefone", max_length=50)
    descricao = forms.CharField(label="Message", widget=forms.Textarea())
