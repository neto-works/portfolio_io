from django import forms
from .models import Contato  #


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato  # Substitua Contato pelo nome correto do seu modelo
        fields = ["nome", "cidade", "email", "telefone", "descricao"]

    def save(self, commit=True):
        instancia = super(ContatoForm, self).save(commit=False)
        # Faça quaisquer modificações adicionais na instância, se necessário
        if commit:
            instancia.save()
        return instancia
