from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # directs to methods to render ALL respective objects
    path('get_areas/', views.get_areas, name='areas'),
    path('get_all_pathways/', views.get_all_pathways, name='all_pathways'),
    path('get_all_degrees/', views.get_all_degrees, name='all_degrees'),

    # filtered paths
    path('get_pathways/<int:id>', views.get_pathways, name='pathways'),

    # detailed paths  --NOTE-- name given in url is the one that must be used with url keyword in .html file
    path('get_pathway_detail/<int:path_id>', views.get_pathway_detail, name='path_detail'),
    path('get_area_detail/<int:area_id>', views.get_area_detail, name='area_detail'),
    path('get_degree_detail/<int:degree_id>', views.get_degree_detail, name='degree_detail'),
]
