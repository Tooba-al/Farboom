from django.urls import path, re_path
from . import api
from .views import *
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# app_name = "backend"

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Farboom API",
#         default_version='development version',
#         description="Farboom API Documentation",
#         contact=openapi.Contact(email="aliabaditooba@gmail.com"),
#     ),
#     public=True,
#     # permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('', api.application, name='application'),
    # path('', ApplicationCreateView.as_view(), name='application'),
    path('resumes/', api.resume_list, name='resumes'),
    # path('resumes/', ResumeListView.as_view(), name='resumes'),
    path('<uuid:pk>/delete/', api.resume_delete, name='resume_delete'),
    # path('create/', api.resume_create, name='resume_create'),
    ]