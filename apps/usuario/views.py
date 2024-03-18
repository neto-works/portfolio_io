from django.shortcuts import render, redirect
from .forms import CustomUsuariosCreateForm


# Create your views here.
def createuser_view(request):
    if request.method == 'POST':
        form = CustomUsuariosCreateForm(request.POST or None)
        if form.is_valid():
            print("formulario valido")
            form.save()
            return redirect('login')
    else:
        form = CustomUsuariosCreateForm()
    return render(request,"usuarios/register.html",context={'form':form})
