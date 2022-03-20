from django.shortcuts import render
from .models import AreaOfStudy, Pathway, Degree


# Create your views here.
def index(request):
    return render(request, 'finder/index.html')


def get_areas(request):
    areas_of_study = AreaOfStudy.objects.order_by("area_of_study").all()
    return render(request, 'finder/areas_of_study.html', {'areas_of_study': areas_of_study})


def get_all_pathways(request):
    pathways = Pathway.objects.order_by("subject").all()
    return render(request, 'finder/all_pathways.html', {'pathways': pathways})


def get_all_degrees(request):
    degrees = Degree.objects.order_by("revised_date").all()
    return render(request, 'finder/all_degrees.html', {'degrees': degrees})

