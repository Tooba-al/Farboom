from django.urls import path

from . import api


urlpatterns = [
    path('', api.project_list, name='project_list'),
    path('<uuid:pk>/', api.project_detail, name='project_detail'),
    path('<uuid:pk>/delete/', api.project_delete, name='project_delete'),
    path('profile/<uuid:id>/', api.project_list_profile, name='project_list_profile'),
    path('create/', api.project_create, name='project_create'),
]