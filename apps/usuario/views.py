from django.shortcuts import render, redirect
from .forms import CustomUsuariosCreateForm
from django.contrib import messages


# Create your views here.
def createuser_view(request):
    if request.method == 'POST':
        form = CustomUsuariosCreateForm(request.POST or None)
        if form.is_valid():
            messages.success(request,'Usuario ja foi criado com sucesso, volte para pagina de login e tente logar')
            form.save()
            return redirect('login')
    else:
        form = CustomUsuariosCreateForm()
    return render(request,"usuarios/register.html",context={'form':form})
