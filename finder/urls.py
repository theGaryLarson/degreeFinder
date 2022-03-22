from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data_entry/', views.get_data_entry_page, name='data_entry'),

    # directs to methods to render ALL respective pages/objects
    path('get_areas/', views.get_areas, name='areas'),
    path('get_all_pathways/', views.get_all_pathways, name='all_pathways'),
    path('get_all_degrees/', views.get_all_degrees, name='all_degrees'),

    # filtered paths
    path('get_pathways/<int:id>', views.get_pathways, name='pathways'),

    # detailed paths  --NOTE-- name given in url is the one that must be used with url keyword in .html file
    path('get_pathway_detail/<int:path_id>', views.get_pathway_detail, name='path_detail'),
    path('get_area_detail/<int:area_id>', views.get_area_detail, name='area_detail'),
    path('get_degree_detail/<int:degree_id>', views.get_degree_detail, name='degree_detail'),


    # form paths
    path('new_student/', views.new_student, name='new_student'),
    path('new_area/', views.new_area, name='new_area'),
    path('new_pathway/', views.new_pathway, name='new_pathway'),
    path('new_degree/', views.new_degree, name='new_degree'),
    path('new_class/', views.new_class, name='new_class'),


    # authorization paths
    path('login_message/', views.login_message, name='login_message'),
    path('logout_message/', views.logout_message, name='logout_message'),


]
