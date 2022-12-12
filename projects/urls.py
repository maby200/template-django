from django.urls import path
from .views import ProjectsView, CreateProjectView, deleteProject

urlpatterns = [
    path('', ProjectsView.as_view(), name='index'),
    path('create-project',CreateProjectView.as_view(), name='create'),
    path('delete/<int:id>',deleteProject, name='delete')
]
