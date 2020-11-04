from django.shortcuts import render


def home(request):
    return render(request, 'alarma_comunitaria_site/index.html')
