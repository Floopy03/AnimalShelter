from django.contrib import admin
from .models import Kind, Animal


admin.site.register(Animal)
admin.site.register(Kind)