from django.shortcuts import render
from .models import Animal, Kind




def main(request):
    
    all = Animal.objects.all()

    context = {
        'all_animal' : all,
    }

    return render(request, 'content/main.html', context)



def show_all(request):
    
    all = Animal.objects.all()


    context = {
        'animal' : all,
    }

    return render(request, 'content/all_animals.html', context)


def onse_animal(request, animal_pk):
    
    context = {
        'animal': Animal.objects.get(pk = animal_pk),

    }

    return render(request, 'content/onse_animal.html', context)

