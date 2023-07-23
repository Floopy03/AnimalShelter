from django.shortcuts import render
from .models import Animal


def main(request):
    
    all = Animal.objects.all()

    context = {
        'all_animal' : all,
    }

    return render(request, 'content/main.html', context)



def second(request):
    
    all = Animal.objects.all()

    context = {
        'all_animal' : all,
    }

    return render(request, 'content/onse_animal.html', context)


