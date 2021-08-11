from django.contrib import admin
from .models import Fruit

@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'calories')

# admin.site.register(Fruit)