from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from apps.api.models import Snippet


class IsSnippetOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request: Request, _: ViewSet, obj: Snippet) -> bool:
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsSameUserOrAdmin(BasePermission):
    def has_object_permission(self, request: Request, _: APIView, obj: User) -> bool:
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user or request.user.is_staff
