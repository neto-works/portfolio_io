from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUsuarios


class CustomUsuariosCreateForm(UserCreationForm):
    class Meta:
        model = CustomUsuarios
        fields = ("first_name", "last_name", "fone")
        labels = {"username": "Username/E-mail"}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


class CustomUsuariosChangeForm(UserChangeForm):
    class Meta:
        model = CustomUsuarios
        fields = ("first_name", "last_name", "fone")
