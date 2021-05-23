from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')

def eup(request):
    return render(request, 'eup.html')
def ecast(request):
    return render(request, 'ecast.html')