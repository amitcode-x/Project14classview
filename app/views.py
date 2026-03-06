from django.shortcuts import render

from app.models import *

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

class SchoolListView(ListView):
    model = School
    context_object_name = "schools"

class SchoolDetailView(DetailView):
    model = School
    context_object_name = "school"
