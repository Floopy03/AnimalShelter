from django.shortcuts import render



def registration(request):
    return render(request, 'userzone/registration.html')



