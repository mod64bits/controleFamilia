from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserModelForm

def registrar(request):
    if request.method == 'POST':
        form = UserModelForm(request.POST)

        if form.is_valid():
            u = form.save()
            u.set_password(u.password)
            u.save()
            return HttpResponseRedirect('/')
    else:
        form = UserModelForm()

    return render(request, 'usuarios/register.html', {'form': form})
