from django.shortcuts import render
from .forms import FormName


def index(request):
    form = FormName()
    return render(request, 'index.html', {'form': form})

def index1(request):
    form = FormName()
    return render(request, 'user.html', {'form': form})