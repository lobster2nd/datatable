from django.urls import path
from .views import init_db, studies_list, view_studies

urlpatterns = [
    path('init_db/', init_db, name='init_db'),
    path('studies/', studies_list, name='studies_list'),
    path('view_studies/', view_studies, name='view_studies'),
]