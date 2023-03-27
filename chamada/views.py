from django.shortcuts import render

def index(request):
    return render(request, 'chamada/index.html')
