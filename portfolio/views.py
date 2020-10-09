from django.shortcuts import render
from .models import Project  ## import from our dictionary a Project class we created

def home(request):
    projects = Project.objects.all()  # this grabs all the objects from the database that are project objects
    return render(request, 'portfolio/home.html', {'projects': projects})
