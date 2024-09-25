
from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="LuckyDress",
        default_version='v1',
        description="...",
        terms_of_service="http://178.255.222.133:81/",
        contact=openapi.Contact(email="admin@mail.ru"),
        license=openapi.License(name="open"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

start_url = "api/"

urlpatterns = [
    path(start_url+'admin/', admin.site.urls),
    path(start_url+'api-auth/', include('rest_framework.urls')),
    path(start_url+'api-info/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    path(start_url+'', include("api.urls")),
]
