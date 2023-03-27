from django.shortcuts import render
from chamada.models import Chamada

def index(request):
    embaixadores = Chamada.objects.all()
    return render(request, 'chamada/index.html', {"lista": embaixadores})
