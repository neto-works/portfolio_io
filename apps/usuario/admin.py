from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUsuariosChangeForm, CustomUsuariosCreateForm
from .models import CustomUsuarios


@admin.register(CustomUsuarios)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuariosCreateForm
    form = CustomUsuariosChangeForm
    model = CustomUsuarios
    list_display = ("first_name", "last_name", "email", "fone", "is_staff")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Informações pessoais", {"fields": ("first_name", "last_name", "fone")}),
        (
            "Permissoẽs",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Datas importantes",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )
