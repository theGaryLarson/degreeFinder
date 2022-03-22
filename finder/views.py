from django.shortcuts import render, get_object_or_404
from .models import AreaOfStudy, Pathway, Degree
from .forms import AreaOfStudyForm, PathwayForm, DegreeForm, ClassForm, StudentForm
from django.contrib.auth.decorators import  login_required


# Create your views here.
def index(request):
    return render(request, 'finder/index.html')


def get_data_entry_page(request):
    return render(request, 'finder/data_entry.html')


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
    filtered_paths = Pathway.objects.filter(area_id=area_id)
    # todo: play with this 'filterPaths' string to see if it is the key to ref context
    return render(request, 'finder/all_pathways.html', {'filteredPaths': filtered_paths})


# detail views
def get_pathway_detail(request, path_id):
    path = get_object_or_404(Pathway, pk=path_id)
    degrees = Degree.objects.filter(pathway_id=path_id)
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


# form views
@login_required
def new_area(request):
    if request.method == 'POST':
        form = AreaOfStudyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = AreaOfStudyForm()
    else:
        form = AreaOfStudyForm()
    return render(request, 'finder/new_area_of_study.html', {'form': form})


@login_required
def new_pathway(request):
    form = PathwayForm
    if request.method == 'POST':
        form = PathwayForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = PathwayForm()
    else:
        form = PathwayForm()
    return render(request, 'finder/new_pathway.html', {'form': form})


@login_required
def new_degree(request):
    form = DegreeForm
    if request.method == 'POST':
        form = DegreeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = DegreeForm()
    else:
        form = DegreeForm()
    return render(request, 'finder/new_degree.html', {'form': form})


@login_required
def new_class(request):
    form = ClassForm
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = ClassForm()
    else:
        form = ClassForm()
    return render(request, 'finder/new_class.html', {'form': form})


# no login required for a student to create a profile
def new_student(request):
    form = StudentForm
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = StudentForm()
    else:
        form = StudentForm()
    return render(request, 'finder/new_student.html', {'form': form})


# authorization views
def login_message(request):
    return render(request, 'finder/login_message.html')


def logout_message(request):
    return render(request, 'finder/logout_message.html')
