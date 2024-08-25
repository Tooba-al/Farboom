# from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

from django.urls import path, re_path
from . import api
from .views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

app_name = "backend"

schema_view = get_schema_view(
    openapi.Info(
        title="Farboom API",
        default_version='development version',
        description="Farboom API Documentation",
        contact=openapi.Contact(email="aliabaditooba@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('me/', api.me, name='me'),
    path('users/', api.users_list, name='users_list'),
    path('profile/', api.profile, name='prfile'),
    path('signup/', api.signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('editprofile/', api.editprofile, name='editprofile'),
    path('editpassword/', api.editpassword, name='editpassword'),
    # path('friends/suggested/', api.my_friendship_suggestions, name='my_friendship_suggestions'),
    # path('friends/<uuid:pk>/', api.friends, name='friends'),
    # path('friends/<uuid:pk>/request/', api.send_friendship_request, name='send_friendship_request'),
    # path('friends/<uuid:pk>/<str:status>/', api.handle_request, name='handle_request'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]