from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse('Hello World!')
    return render(request, 'home.html')

def contact(request):
    #return HttpResponse('Hello World!')
    return render(request, 'contact.html', {'usuario': 'Fulano de Tal'})