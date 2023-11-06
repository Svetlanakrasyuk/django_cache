from django.shortcuts import render
from django.views.generic import ListView

from .models import MyModel


class ShowHome(ListView):
    model = MyModel
    template_name = "myapp/home.html"
    context_object_name = "my_context"
