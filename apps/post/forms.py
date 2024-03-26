from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','descricao','likes','imagem','blogueiro_id']
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),  # Defina a classe CSS e as propriedades desejadas
        }

class AHPfForm():
    ...