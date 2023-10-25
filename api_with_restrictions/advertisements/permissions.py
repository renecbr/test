from rest_framework.permissions import BasePermission

from django.contrib.auth.models import User


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET' or request.user.is_staff is True:
            return True
        return request.user == obj.creator