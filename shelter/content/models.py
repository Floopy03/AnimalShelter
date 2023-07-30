from django.db import models
from django.urls import reverse


class Kind(models.Model):
    name = models.CharField(max_length = 30)


    def __str__(self):
        return self.name 
    

class Animal(models.Model):

    SEX_CHOICES = [
        ("B", "Boy"),
        ("G", "Girl"),
    ]

    kind = models.ForeignKey(Kind, on_delete = models.PROTECT, null = True)
    sex = models.CharField(max_length = 1, choices = SEX_CHOICES, default = 'B')
    name = models.CharField(max_length = 30)
    old = models.IntegerField(default = 1)
    description = models.TextField()                    #550
    photo = models.ImageField(null = True, blank = True, upload_to = 'images/')


    def __str__(self):
        return self.name
    
    def age(self):
        if self.old >= 12:
            return f'{round(self.old/12, 1)} років'
        else:
            if self.old == 1:
                return f'{self.old} місяць'
            if self.old < 5:
                return f'{self.old} місяці'
            else:
                return f'{self.old} місяців'
            
    def gender(self):
        return 'Хлопчик' if self.sex == 'B' else 'Дівчинка'
    
    def treat_for_animal(self):
        if self.name[-1] == 'а':
            return self.name[0:-1] + 'у'
        
        if self.name[-1] == 'я':
            return self.name[0:-1] + 'ю'

        else:
           return self.name

            

    def get_absolute_url(self):
        return reverse("one_animal", kwargs = {'animal_pk': self.pk})


                

