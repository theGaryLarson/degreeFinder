from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # directs to methods to render ALL respective objects
    path('get_areas/', views.get_areas, name='areas'),
    path('get_all_pathways/', views.get_all_pathways, name='all_pathways'),
    path('get_all_degrees/', views.get_all_degrees, name='all_degrees'),
]
