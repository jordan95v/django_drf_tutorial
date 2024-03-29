from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from rest_framework.views import APIView
from apps.api.models import Snippet


class IsSnippetOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request: Request, _: APIView, obj: Snippet) -> bool:
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user
