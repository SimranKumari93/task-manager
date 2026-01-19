from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsAdminOrOwner

# class TaskViewSet(ModelViewSet):
#     serializer_class = TaskSerializer
#     permission_classes = [IsAuthenticated, IsAdminOrOwner]

#     def get_queryset(self):
#         user = self.request.user
#         if user.role == 'admin':
#             return Task.objects.all()
#         return Task.objects.filter(assigned_to=user)


from rest_framework.exceptions import PermissionDenied

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Task.objects.all()
        return Task.objects.filter(assigned_to=user)

    def perform_create(self, serializer):
        if self.request.user.role != 'admin':
            raise PermissionDenied("Only admin can create tasks")
        serializer.save()
