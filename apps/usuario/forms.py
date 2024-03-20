from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUsuarios
from django import forms


class CustomUsuariosCreateForm(UserCreationForm):
    class Meta:
        model = CustomUsuarios
        fields = ('first_name', 'last_name','username','fone')
        labels = {'username': 'Username/E-mail'}
        widgets = {
            'fone': forms.TextInput(attrs={'placeholder': 'ex: +5584981117731'}),
            'username': forms.TextInput(attrs={'placeholder': 'exemplo@gmail.com'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['username']
        if commit:
            user.save()
        return user


class CustomUsuariosChangeForm(UserChangeForm):
    class Meta:
        model = CustomUsuarios
        fields = ('first_name', 'last_name', 'fone')
