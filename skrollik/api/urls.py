from django.urls import path, include
from django.contrib.auth import views as auth_views  

from .views import (
    AuthorizationView,
    UserRegisterView,
    OrderViewset,
    CategoryViewset,
    OrderAccept,
    OrderClose,
)

urlpatterns = [
    path('login/', AuthorizationView.as_view(), name='login'),

    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('orders', OrderViewset.as_view({"get":"list"})),
    path('orders/', OrderViewset.as_view({"post":"create"})),
    path('orders/<int:pk>', OrderViewset.as_view({"get":"retrieve", "put": "update", "delete": "destroy"})),
    path('categories', CategoryViewset.as_view({"get":"list"})),

    path('orders/<int:pk>/accept/', OrderAccept.as_view()),
    path('orders/<int:pk>/close/', OrderClose.as_view()),
]