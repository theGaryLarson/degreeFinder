from django.shortcuts import render, get_object_or_404
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


# filtered views
def get_pathways(request, area_id):
    """
    use a for loop to iterate through objects in .html file
    :param request: request object handled by django
    :param area_id: id of area-of-study
    :return: list of Pathways under that area of study
    """
    filtered_paths = Pathway.objects.filter(area=area_id)
    # todo: play with this 'filterPaths' string to see if it is the key to ref context
    return render(request, 'finder/all_pathways.html', {'filteredPaths': filtered_paths})


# detail views
def get_pathway_detail(request, path_id):
    path = get_object_or_404(Pathway, pk=path_id)
    degrees = Degree.objects.filter(pathway_id=path.pk)
    context = {
        'path': path,
        'degrees': degrees
    }
    return render(request, 'finder/pathway_detail.html', {'context': context})


def get_area_detail(request, area_id):
    area = get_object_or_404(AreaOfStudy, pk=area_id)
    return render(request, 'finder/area_of_study_detail.html', {'area': area})


def get_degree_detail(request, degree_id):
    degree = get_object_or_404(Degree, pk=degree_id)
    return render(request, 'finder/degree_detail.html', {'degree': degree})