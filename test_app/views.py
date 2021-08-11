from django.shortcuts import render
from django.views.generic import ListView

from .models import Fruit

class FruitsView(ListView):
    model = Fruit
    queryset = Fruit.objects.all()
    template_name = "test_app/fruits.html"

