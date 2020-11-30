from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'user': 'fulano'
    }
    return render(request, 'home.html', context)

def contato(request):
    return render(request, 'contato.html')