from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from .models import User, Employee, Role, RolePermission, UserRole
from .serializers import (
    UserSerializer, EmployeeSerializer, RoleSerializer,
    RolePermissionSerializer, UserRoleSerializer
)

@extend_schema(tags=["User - Foydanluvchilarni ko'rish "])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@extend_schema(tags=["Employee - Barcha ishchilarni ko'rish "])
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

@extend_schema(tags=["Role - Ishchilarga mavjud rollarni ko'rish  "])
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

@extend_schema(tags=["RolePermission - Rollarga berilgan ruxsatlarni ko'rish "])
class RolePermissionViewSet(viewsets.ModelViewSet):
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer

@extend_schema(tags=["UserRole - Foydanluvchiga berilgan ruxsatlarni ko'rish "])
class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer