from django.shortcuts import render
from .models import Animal, Kind



def main(request):
    
    all = Animal.objects.all()

    context = {
        'all_animal' : all,
    }

    return render(request, 'content/main.html', context)



def second(request):
    
    all = Animal.objects.all()
    kind_of = Kind.objects.all()

    context = {
        'animal' : all,
        'kind' : kind_of,
    }

    return render(request, 'content/all_animals.html', context)


