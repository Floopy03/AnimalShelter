from django.db import models


class Kind(models.Model):
    name = models.CharField(max_length = 30)


    def __str__(self):
        return self.name 
    

class Animal(models.Model):

    SEX_CHOICES = [
        ("B", "Boy"),
        ("G", "Girl"),
    ]

    kind = models.ManyToManyField(Kind)
    sex = models.CharField(max_length = 1, choices = SEX_CHOICES, default = 'B')
    name = models.CharField(max_length = 30)
    description = models.TextField()
    photo = models.ImageField(null = True, blank = True, upload_to = 'images/')


    def __str__(self):
        return self.name 


