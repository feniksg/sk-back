from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
from django.contrib.auth import login
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend


from rest_framework.authtoken.models import Token
from rest_framework import status, permissions, generics, viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from rest_framework.filters import OrderingFilter

from .serializers import (
    AuthorizationSerializer,
    CustomUserMinSerializer,
    UserRegisterSerializer,
    OrderMinSerializer,
    OrderSerializer,
    OrderCategorySerializer
)

from .models import (
    Order,
    OrderCategory,
    OrderStatusChoices,
    CustomUser
)

from .paginators import (
    I50ResultsSetPagination
)

from .filters import OrderFilter

from drf_yasg.utils import swagger_auto_schema


class CSRFToken(APIView):
    permission_classes = [permissions.AllowAny]
    
    @method_decorator(ensure_csrf_cookie)
    def get(self, request, format=None):
        csrf_token = get_token(request)
        return JsonResponse({'csrfToken': csrf_token})


class AuthorizationView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(request_body=AuthorizationSerializer)
    def post(self, request, *args, **kwargs):
        serializer = AuthorizationSerializer(data=self.request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            data = {
                'user': CustomUserMinSerializer(user).data,
                'token': token.key,
            }
            return Response(data=data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=serializer.errors['non_field_errors'][0].code)
    

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.filter(status=OrderStatusChoices.PENDING)
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer
    pagination_class = I50ResultsSetPagination
    filter_backends = (DjangoFilterBackend,OrderingFilter) 
    filterset_class = OrderFilter  
    ordering_fields = ['created_at', 'payment'] 
    ordering = ['created_at']

    def list(self, request, *args, **kwargs):
        self.serializer_class = OrderMinSerializer
        return super().list(request, *args, **kwargs)

class CategoryViewset(viewsets.ModelViewSet):
    queryset = OrderCategory.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderCategorySerializer

class OrderAccept(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request:Request, pk):
        current_order = Order.objects.filter(pk=pk).first()
        if current_order:
            current_order.status = OrderStatusChoices.IN_WORK
            current_order.performer = request.user
            current_order.save()

            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_404_NOT_FOUND)

class OrderClose(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request:Request, pk):
        current_order = Order.objects.filter(pk=pk).first()
        if current_order:
            if current_order.customer.pk == request.user.pk:
                current_order.status = OrderStatusChoices.CLOSED
                current_order.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_404_NOT_FOUND)


