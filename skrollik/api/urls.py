from django.urls import path
from django.contrib.auth import views as auth_views  

from .views import (
    AuthorizationView,
    UserRegisterView,
    OrderViewset,
    CategoryViewset,
    OrderAccept,
    OrderClose,
    MyInfoView,
    CustomUserViewSet,
    OrderSearchListView
)

urlpatterns = [
    path('login/', AuthorizationView.as_view(), name='login'),

    path('me', MyInfoView.as_view()),
    path('users/<int:pk>', CustomUserViewSet.as_view({"get":"retrieve"})),  

    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('orders', OrderViewset.as_view({"get":"list"})),
    path('orders/', OrderViewset.as_view({"post":"create"})),
    path('orders/<int:pk>', OrderViewset.as_view({"get":"retrieve", "put": "update", "delete": "destroy"})),
    path('categories', CategoryViewset.as_view({"get":"list"})),

    path('orders/search', OrderSearchListView.as_view()),
    path('orders/<int:pk>/accept/', OrderAccept.as_view()),
    path('orders/<int:pk>/close/', OrderClose.as_view()),
]